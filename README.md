# PyTapir

Python flavored [tapir](https://github.com/stroeer/tapir/) output of `protoc`.

A general [API documentation can be found here](https://stroeer.github.io/tapir/).

(Disclaimer: this is my very first python module ever)

# Installation

## `pipenv`

[untested]

`pipenv install -e git+https://github.com:stroeer/pytapir.git@b937708bf3e642b8cf50a74136f2088cbf520ea9#egg=requests`

## `pipenv`

This should go into the `Pipfile`

```shell
[packages]
boto3 = "*"
pytapir = { git = "git@github.com:stroeer/pytapir.git", ref = "b937708bf3e642b8cf50a74136f2088cbf520ea9"}
```

# Release

```shell
NEXT_TAG='v0.0.1'

# bump tapir to latest
git submodule update --init --recursive

# commit changes
git commit -a -m "bumped tapir to latest"

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
      https://api.github.com/repos/stroeer/tapir/releases
fi
```