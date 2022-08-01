FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

ADD sh_deploy/nginx_ssl.sh /nginx_ssl.sh
RUN chmod +x /django.sh
