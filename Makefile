NEXT_TAG 	:= $(shell git submodule foreach git describe --tags | grep -v 'Entering' | awk -F- '//{print $$1}' | cut -c 2-)
ACCOUNT_ID 	:= $(eval ACCOUNT_ID := $(shell aws --output text sts get-caller-identity --query "Account"))$(ACCOUNT_ID)

bump_tapir:
	# bump tapir to latest
	git submodule update --init --recursive
	git submodule foreach git fetch --all --tags --prune
	git submodule foreach git pull origin main

	# commit changes
	git add tapir

	# if there are changes, commit and push them:
	git commit -m "bumped tapir to latest (origin/main)"
	git push

release:
	sed -i "" "s/__version__ = .*/__version__ = \"$(NEXT_TAG)\"/" stroeer/__init__.py
	
	# pull latest from remote
	git fetch --all --tags --prune
	git switch main

	# compile protobuf sources to python
	python3 setup.py install
	python3 setup.py protoc

	# commit changes
	git commit -a -m "release version $(NEXT_TAG)"

	# tag commit
	git tag -a "$(NEXT_TAG)" -m "$(NEXT_TAG)"

	# push tag
	git push origin $(NEXT_TAG)

	# release commit
	if [ ! -z "$${GITHUB_TOKEN}" ] ; then \
	    curl -X POST \
	      --header "Authorization: token $${GITHUB_TOKEN}" 	\
	      --header "Accept: application/vnd.github.v3+json"	\
	      --data "{\"tag_name\":\"$(NEXT_TAG)\",\"generate_release_notes\":true}" \
	      https://api.github.com/repos/stroeer/pytapir/releases \
	fi

lambda_layer:
	echo "building lambda layer for $(NEXT_TAG)"
	set -euo pipefail ; \
	for PYTHON_VERSION in 3.11 3.12 ; do \
	  for ARCH in arm64 x86_64 ; do	\
	    docker buildx build --load \
	    	--platform linux/$${ARCH} \
	    	--build-arg="PYTHON_VERSION=$${PYTHON_VERSION}" \
	    	--tag "$(NEXT_TAG):$${ARCH}" \
	    	--file dockerfiles/$${PYTHON_VERSION}/Dockerfile . ; \
	    	LAYER_FILE_ZIP="layer_$${ARCH}_$${PYTHON_VERSION}_layer.zip" ; \
	    docker run --platform linux/$${ARCH} --rm --entrypoint cat "$(NEXT_TAG):$${ARCH}" layer.zip > $${LAYER_FILE_ZIP}  ; \
	    aws s3 cp $${LAYER_FILE_ZIP} s3://ci-$(ACCOUNT_ID)-eu-west-1/pytapir/$${LAYER_FILE_ZIP} ; \
	    if [ "$$ARCH" = "x86_64" ] ; then \
	      ARCH_Pretty='Amd64' ; \
	    else \
	      ARCH_Pretty='Arm64' ; \
	    fi ; \
	    layer_version=$$(aws lambda publish-layer-version \
	      --layer-name PyTapir-$${ARCH_Pretty} \
	      --description "PyTapir $(NEXT_TAG)" \
	      --license-info "MIT" \
	      --content S3Bucket=ci-$(ACCOUNT_ID)-eu-west-1,S3Key=pytapir/$${LAYER_FILE_ZIP} \
	      --compatible-runtimes python$${PYTHON_VERSION} \
	      --compatible-architectures $${ARCH} \
	      --query "Version") ; \
	    org_id=$$(aws organizations describe-organization --query 'Organization.Id' --output text) ; \
	    aws lambda add-layer-version-permission \
	      --layer-name PyTapir-$${ARCH_Pretty} \
	      --statement-id xaccount \
	      --action lambda:GetLayerVersion \
	      --organization-id "$${org_id}" \
	      --principal '*' \
	      --version-number "$${layer_version}" ; \
	  done ; \
	done