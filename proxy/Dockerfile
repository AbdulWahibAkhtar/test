FROM nginx:1.13-alpine
COPY conf /etc/nginx/nginx.conf.tmp
COPY rootCA.pem /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/
index  insert.html index.html index.html   
COPY index usr/share/nginx/html
