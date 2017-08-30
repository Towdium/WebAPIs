#!/bin/bash

cd /
rm -rf WebAPIs
rm -rf centos-nginx-gunicorn
git clone https://github.com/Towdium/WebAPIs.git
git clone https://github.com/Towdium/centos-nginx-gunicorn.git
rm -rf centos-nginx-gunicorn/app
mv WebAPIs centos-nginx-gunicorn/app
docker build -t centos-nginx-gunicorn .
docker stop server
docker rm server
docker run -p 80:80 -d --restart unless-stopped --name server centos-nginx-gunicorn
