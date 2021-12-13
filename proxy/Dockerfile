FROM nginx:1.13-alpine
COPY conf /etc/nginx/conf.d/default.conf


COPY rootCA.pem /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/
