FROM nginx:1.13-alpine
COPY conf /etc/nginx/nginx.conf.tmp
COPY rootCA.pem /etc/nginx/nginx/ssl/
COPY site.ctr /etc/nginx/nginx/ssl/
