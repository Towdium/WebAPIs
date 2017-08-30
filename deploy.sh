#!/bin/bash
set -x

cd ~/
rm -rf WebAPIs
rm -rf centos-nginx-gunicorn
git clone https://github.com/Towdium/WebAPIs.git
git clone https://github.com/Towdium/centos-nginx-gunicorn.git
rm -rf centos-nginx-gunicorn/app
mv WebAPIs/deploy.sh ~/deploy.sh
mv WebAPIs centos-nginx-gunicorn/app
cd centos-nginx-gunicorn/
docker build -t centos-nginx-gunicorn .
docker stop server
docker rm server
docker run -p 80:80 -d --restart unless-stopped --name server centos-nginx-gunicorn
rm -rf ~/centos-nginx-gunicorn
