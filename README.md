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
pytapir = { git = "git@github.com:stroeer/pytapir.git", ref = "v0.30.0"}
```

## Lambda layers

Permissions should allow every account within our AWS organization to access the
pytapir lambda layers.

The lambda layer contains everything you'll need to invoke our gRPC services. See 
`./examples/` folder for sample code. 

- `pytapir`
- [`grpcio`](https://pypi.org/project/grpcio/)

| tapir version |                           ARN                           |
|:-------------:|:-------------------------------------------------------:|
|    0.29.1     | `arn:aws:lambda:eu-west-1:053041861227:layer:pytapir:5` |
|    0.30.0     | `arn:aws:lambda:eu-west-1:053041861227:layer:pytapir:6` |

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
git submodule foreach git pull origin master

# commit changes
git add tapir

# if there are changes, commit and push them:
git commit -m "bumped tapir to latest (origin/master)"
git push

```

# Release

bump version in [__init__.py](./stroeer/__init__.py), ideally to match the version of tAPIr.

```shell
NEXT_TAG=$(echo "import stroeer; print(stroeer.__version__)" | python3)

# pull latest from remote
git fetch --all --tags --prune
git switch main

# compile protobuf sources to python
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
rm -rf python/ || true
mkdir -p "python"
# download all requirements into a directory "python" using 
# a sandboxed local environment that replicates the live AWS Lambda environment almost identically
# https://github.com/lambci/docker-lambda
docker run --rm \
  --volume "${PWD}":/var/task \
  lambci/lambda:build-python3.8 pip install --requirement requirements.txt --target python

# add our sources
cp -R stroeer python/

# zip all the things
zip --recurse-paths --verbose layer.zip python

NEXT_TAG=$(echo "import stroeer; print(stroeer.__version__)" | python3)
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

aws s3 cp layer.zip s3://ci-${ACCOUNT_ID}-eu-west-1/pytapir/layer_${NEXT_TAG}.zip

# configure your aws environment here
#alias AWS='aws'
alias AWS='aws-vault exec to -- aws'

# create lambda layer
layer_version=$(AWS lambda publish-layer-version \
  --layer-name pytapir \
  --description "pytapir ${NEXT_TAG}" \
  --license-info "MIT" \
  --content S3Bucket=ci-${ACCOUNT_ID}-eu-west-1,S3Key=pytapir/layer_${NEXT_TAG}.zip \
  --compatible-runtimes python3.8 \
  --compatible-architectures "x86_64" \
  --query "Version")

# allow aws org to access layer
org_id=$(AWS organizations describe-organization --query 'Organization.Id' --output text)

AWS lambda add-layer-version-permission \
  --layer-name pytapir \
  --statement-id xaccount \
  --action lambda:GetLayerVersion \
  --organization-id "${org_id}" \
  --principal '*' \
  --version-number "${layer_version}" 
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
