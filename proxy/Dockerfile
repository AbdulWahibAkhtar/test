FROM nginx:1.13-alpine
COPY rootCA.pem /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/
COPY insert.html /usr/share/nginx/html/   
COPY select.html /usr/share/nginx/html/   
COPY conf /etc/nginx/nginx.conf.tmp



