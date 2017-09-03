#!/bin/bash
set -x

mkdir /tmp/deploy
cd /tmp/deploy
git clone https://github.com/Towdium/WebAPIs.git
git clone https://github.com/Towdium/nginx-gunicorn.git
rm -rf nginx-gunicorn/app
mv WebAPIs nginx-gunicorn/app
cd nginx-gunicorn/
docker build -t alpine-nginx-gunicorn .
docker stop server
docker rm server
docker run -p 80:80 -d --restart unless-stopped --name server alpine-nginx-gunicorn
rm -rf /tmp/deploy
