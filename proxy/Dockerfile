FROM nginx:1.13-alpine
COPY conf /etc/nginx/nginx.conf.tmp
COPY /certs/rootCA.pem /etc/nginx/ssl/
COPY /certs/site.crt /etc/nginx/ssl/
COPY /html/insert.html usr/share/nginx/html/
COPY /html/select.html usr/share/nginx/html/