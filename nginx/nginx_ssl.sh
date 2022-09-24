#!/bin/bash -x

apt update && apt-get install letsencrypt
apt-get install python3-certbot-nginx

certbot --nginx -d api.quicksmart.pro
