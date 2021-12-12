FROM nginx:1.13-alpine
COPY conf /etc/nginx/conf.d/default.conf
COPY rootCA.crt /etc/nginx/ssl/
COPY rootCA.key /etc/nginx/ssl/
COPY rootCA.pem /etc/nginx/ssl/
COPY rootCA.csr /etc/nginx/ssl/
COPY site.csr /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/
COPY site.key /etc/nginx/ssl/
COPY ssl-bundle.crt /etc/nginx/ssl/
COPY v3.ext /etc/nginx/ssl/