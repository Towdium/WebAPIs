#!/bin/bash
set -x

mkdir /tmp/deploy
cd /tmp/deploy
git clone https://github.com/Towdium/WebAPIs.git
git clone https://github.com/Towdium/alpine-nginx-gunicorn.git
cp -r /home/towdium/Documents/Dev/WebAPIs ./WebAPIs
cp -r /home/towdium/Documents/Dev/alpine-nginx-gunicorn alpine-nginx-gunicorn
rm -rf alpine-nginx-gunicorn/app
mv WebAPIs alpine-nginx-gunicorn/app
cd alpine-nginx-gunicorn/
docker build -t alpine-nginx-gunicorn .
docker stop server
docker rm server
docker run -p 80:80 -d --restart unless-stopped --name server alpine-nginx-gunicorn
rm -rf /tmp/deploy
