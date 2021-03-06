#!/bin/bash
set -x

proxy=$(ip route get 1 | awk '{print $NF;exit}')
mkdir /tmp/deploy
cd /tmp/deploy
cp -r /home/towdium/Documents/Dev/WebAPIs ./WebAPIs
cp -r /home/towdium/Documents/Dev/nginx-gunicorn nginx-gunicorn
rm -rf nginx-gunicorn/app
mv WebAPIs nginx-gunicorn/app
cd nginx-gunicorn/
docker build --build-arg HTTP_PROXY=http://$proxy:1080 -t alpine-nginx-gunicorn .
docker stop server
docker rm server
docker run -p 80:80 -d --restart unless-stopped --name server \
-e HTTP_PROXY=http://$proxy:1080 alpine-nginx-gunicorn
rm -rf /tmp/deploy
