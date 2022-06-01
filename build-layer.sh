#!/bin/bash

# Taken from: https://aws.amazon.com/premiumsupport/knowledge-center/lambda-layer-simulated-docker/

build_layer_zip() {
    check_preconditions

    echo "Creating pytapir AWS Lambda layer"

    echo "Installing dependencies..."
    install_deps_for_version 3.9 > /dev/null
    install_deps_for_version 3.8 > /dev/null 
    install_deps_for_version 3.7 > /dev/null

    echo "Creating ZIP archive..."
    zip -r layer.zip python > /dev/null

    echo "Cleaning up..."
    rm -r python

    ls -lah layer.zip
    echo "Done."
}


check_preconditions() {
    assert_file_exists "${PWD}/requirements.txt"
    warn_file_exists "layer.zip"
    assert_docker_running
}


install_deps_for_version() {
    VERSION="${1}"

    docker run  \
        -v "${PWD}":/var/task \
        -e PIP_DISABLE_PIP_VERSION_CHECK=1 \
        "public.ecr.aws/sam/build-python${VERSION}:latest" \
        /bin/sh -c "pip install -r requirements.txt -t python/lib/python${VERSION}/site-packages/"
}


assert_file_exists() {
    if [[ ! -f ${1} ]]; then
        echo "Error: Requires file '${1}' to exist."
        exit 1
    fi
}


warn_file_exists() {
    if [[ -f ${1} ]]; then
        echo "Warning: File '${1}' already exists, proceeding anyway."
    fi
}


assert_docker_running() {
    if ! docker info > /dev/null 2>&1; then
        echo "Error: Requires Docker to run."
        exit 1
    fi
}


build_layer_zip
