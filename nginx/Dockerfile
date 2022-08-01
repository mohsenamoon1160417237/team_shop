FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

ADD mime.types /etc/nginx/mime.types
RUN chmod +x /etc/nginx/mime.types

ADD nginx_ssl.sh /nginx_ssl.sh
RUN chmod +x /nginx_ssl.sh
