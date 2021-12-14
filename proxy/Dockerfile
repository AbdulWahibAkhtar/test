FROM nginx:1.13-alpine
COPY conf /etc/nginx/conf.d/default.conf
COPY rootCA.pem /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/

location/ {            
        root/usr/share/nginx/html;
        html/insert.html;
        html/select.html;

        index  insert.html:50   
        person {proxy_pass http://backend:5000;}
        persons {proxy_pass http://backend:5000;}
}
