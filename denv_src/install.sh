#!/bin/bash

# Check if a custom Docker image name is provided as an argument
if [ "$#" -eq 1 ]; then
    docker_image_name="$1"
else
    docker_image_name="denv"
fi

docker build -t "$docker_image_name" .

cp denv.py /usr/local/bin/denv
chmod +x /usr/local/bin/denv

echo "Docker image and denv script installed successfully with image name: $docker_image_name"
 
