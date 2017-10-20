#!/bin/bash
set -x

mkdir /tmp/deploy
cd /tmp/deploy
git clone https://github.com/Towdium/WebAPIs.git
git clone -b alpine-nginx-gunicorn https://github.com/Towdium/DockerImages.git
rm -rf DockerImages/app
mv WebAPIs DockerImages/app
cd DockerImages/
docker build -t alpine-nginx-gunicorn .
docker stop server
docker rm server
docker run -p 80:80 -d --restart unless-stopped --name server alpine-nginx-gunicorn
rm -rf /tmp/deploy
