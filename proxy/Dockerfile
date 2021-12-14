FROM nginx:1.13-alpine
COPY /conf /etc/nginx/nginx.conf.tmp
COPY /rootCA.pem /etc/nginx/ssl/
COPY /site.crt /etc/nginx/ssl/
COPY /insert.html /etc/nginx/html/   
COPY /select.html /etc/nginx/html/   
COPY /index usr/share/nginx/html
