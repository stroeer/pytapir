# PyTapir

Python flavored [tapir](https://github.com/stroeer/tapir/) output of `protoc`.

A general [API documentation can be found here](https://stroeer.github.io/tapir/).

(Disclaimer: this is my very first python module ever)

# Usage

_pytapir_ is usually distributed via python packages that are hosted on GitHub. We're trying to have the
latest version available all the time; but since python is more of a side project we cannot keep that
promise.

In case this library diverges from the tAPIr-API, please give me (@thisismana) a bump to fix this.

## `pipenv`

`pipenv install -e git+https://github.com:stroeer/pytapir.git@v0.30.0#egg=requests`

## `Pipfile`

This should go into the `Pipfile`

```shell
[packages]
pytapir = { git = "git@github.com:stroeer/pytapir.git", ref = "v0.40.0"}
```

## Lambda layers

Permissions should allow every account within our AWS organization to access the
pytapir lambda layers.

The lambda layer contains everything you'll need to invoke our gRPC services. See
`./examples/` folder for sample code.

- `pytapir`
- [`grpcio`](https://pypi.org/project/grpcio/)

| tapir version | Python Version | Arch   |                                ARN                                |
|:-------------:|----------------|--------|:-----------------------------------------------------------------:|
|    0.29.1     | 3.8            | x86_64 |      `arn:aws:lambda:eu-west-1:053041861227:layer:pytapir:5`      |
|    0.30.0     | 3.8            | x86_64 |      `arn:aws:lambda:eu-west-1:053041861227:layer:pytapir:6`      |
|    0.33.1     | 3.8            | x86_64 |      `arn:aws:lambda:eu-west-1:053041861227:layer:pytapir:8`      |
|    0.39.0     | 3.8            | x86_64 |     `arn:aws:lambda:eu-west-1:053041861227:layer:pytapir:11`      |
|    0.40.0     | 3.8            | x86_64 |     `arn:aws:lambda:eu-west-1:053041861227:layer:pytapir:12`      |
|    0.41.0     | 3.11           | x86_64 |   `arn:aws:lambda:eu-west-1:053041861227:layer:PyTapir-Amd64:1`   |
|    0.41.0     | 3.11           | amd64  |   `arn:aws:lambda:eu-west-1:053041861227:layer:PyTapir-Arm64:1`   |
|    0.42.2     | 3.11           | amd64  | `arn:aws:lambda:eu-west-1:053041861227:layer:PyTapir-311-Arm64:1` |
|    0.42.2     | 3.11           | x86_64 | `arn:aws:lambda:eu-west-1:053041861227:layer:PyTapir-311-Amd64:1` |
|    0.42.2     | 3.12           | amd64  | `arn:aws:lambda:eu-west-1:053041861227:layer:PyTapir-312-Arm64:1` |
|    0.42.2     | 3.12           | x86_64 | `arn:aws:lambda:eu-west-1:053041861227:layer:PyTapir-312-Amd64:1` |

# Build tapir

## dependencies

We're using a _virtual env_, so do the following within the project root after cloning this repo:

```shell 
$ python3 -m venv pytapir
$ source pytapir/bin/activate
$ pip install --requirement requirements.txt

# you can work now, e.g. compile .proto to .py
$ python3 setup.py protoc

# once your done, deactivate the venv
$ deactivate
````

## bump tapir submodule

tapir is mounted as a git submodule

```shell
# bump tapir to latest
git submodule update --init --recursive
git submodule foreach git fetch --all --tags --prune
git submodule foreach git pull origin main

# commit changes
git add tapir

# if there are changes, commit and push them:
git commit -m "bumped tapir to latest (origin/main)"
git push
```

# Release

```shell
NEXT_TAG=$(git submodule foreach git describe --tags | grep -v 'Entering' | awk -F- '//{print $1}' | cut -c 2-)
sed -i "" "s/__version__ = .*/__version__ = \"${NEXT_TAG}\"/" stroeer/__init__.py

# pull latest from remote
git fetch --all --tags --prune
git switch main

# compile protobuf sources to python
python3 setup.py install
python3 setup.py protoc

# commit changes
git commit -a -m "release version ${NEXT_TAG}"

# tag commit
git tag -a "${NEXT_TAG}" -m "${NEXT_TAG}"

# push tag
git push origin ${NEXT_TAG}

# release commit
if [ ! -z "${GITHUB_TOKEN}" ] ; then
    curl -X POST \
      --header "Authorization: token ${GITHUB_TOKEN}" 	\
      --header "Accept: application/vnd.github.v3+json"	\
      --data "{\"tag_name\":\"${NEXT_TAG}\",\"generate_release_notes\":true}" \
      https://api.github.com/repos/stroeer/pytapir/releases
fi
```

# AWS Lambda Layer

Useful reads:

- [how to build a python lambda layer][howto]
- [Add library dependencies to layer][deps]

[howto]: https://unbiased-coder.com/create-python-lambda-layer/

[deps]: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-path

```shell


NEXT_TAG=$(echo "import stroeer; print(stroeer.__version__)" | python3)
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
for PYTHON_VERSION in 3.11 3.12 ; do
  for ARCH in arm64 x86_64 ; do
    docker buildx build --load --platform linux/${ARCH} --build-arg="PYTHON_VERSION=${PYTHON_VERSION}" --tag "${NEXT_TAG}:${ARCH}" .
  
    docker run --platform linux/${ARCH} --rm --entrypoint cat "${NEXT_TAG}:${ARCH}" layer.zip > ${ARCH}_layer.zip
    
    aws s3 cp ${ARCH}_layer.zip s3://ci-${ACCOUNT_ID}-eu-west-1/pytapir/layer_${NEXT_TAG}_${ARCH}.zip
    
    if [ "$ARCH" = "x86_64" ] ; then
      ARCH_Pretty='Amd64'
    else
      ARCH_Pretty='Arm64'
    fi
    
    # create lambda layer
    layer_version=$(aws lambda publish-layer-version \
      --layer-name PyTapir-${ARCH_Pretty} \
      --description "PyTapir ${NEXT_TAG}" \
      --license-info "MIT" \
      --content S3Bucket=ci-${ACCOUNT_ID}-eu-west-1,S3Key=pytapir/layer_${NEXT_TAG}_${ARCH}.zip \
      --compatible-runtimes python${PYTHON_VERSION} \
      --compatible-architectures ${ARCH} \
      --query "Version")
    
    # allow aws org to access layer
    org_id=$(aws organizations describe-organization --query 'Organization.Id' --output text)
    
    aws lambda add-layer-version-permission \
      --layer-name PyTapir-${ARCH_Pretty} \
      --statement-id xaccount \
      --action lambda:GetLayerVersion \
      --organization-id "${org_id}" \
      --principal '*' \
      --version-number "${layer_version}" 
  done  
done  
```

# Release 2024 version

```shell
# update submodule
make bump_tapir
# create python github release
make release
# build lambda layer for python 3.11/3.12 for amd64/arm64
make lambda_layer
```

## Local testing lambda and lambda layer

To test, we need:

- an environment that replicates the AWS environment
  (e.g. don't use native MacOS binaries).
- our lambda layer mounted
- our sample code mounted

```shell
export GRPC_ENDPOINT="$(aws ssm get-parameter --name /internal/api/endpoint --with-decryption --query 'Parameter.Value' --output text)"
export GRPC_AUTHORIZATION="Bearer $(aws ssm get-parameter --name /internal/api/auth.token --with-decryption --query 'Parameter.Value' --output text)"
docker run --rm \
  --volume "${PWD}/examples":/var/task:ro \
  --volume "${PWD}/python":/opt/python:ro \
  --env GRPC_ENDPOINT \
  --env GRPC_AUTHORIZATION \
  lambci/lambda:python3.8 lambda_function.lambda_handler
```
