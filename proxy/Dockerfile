FROM nginx:1.13-alpine
COPY conf /etc/nginx/conf.d/default.conf
COPY rootCA.pem /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/
COPY /html/insert.html:/81  

location/ {            
        root/usr/share/nginx/html:81;
        html/insert.html:81
        html/select.html:81

        index  insert.html:50   
        person {proxy_pass http://backend:5000;}
        persons {proxy_pass http://backend:5000;}
}
