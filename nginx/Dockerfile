FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

ADD nginx_ssl.sh /nginx_ssl.sh
RUN chmod +x /nginx_ssl.sh
