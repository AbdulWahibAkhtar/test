FROM python:3.8-alpine

COPY rootCA.crt /etc/nginx/ssl/
COPY rootCA.key /etc/nginx/ssl/
COPY rootCA.pem /etc/nginx/ssl/
COPY rootCA.csr /etc/nginx/ssl/
COPY site.csr /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/
COPY site.key /etc/nginx/ssl/
COPY ssl-bundle.crt /etc/nginx/ssl/ 

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/
ENV FLASK_APP app.py
ENV FLASK_ENV development
CMD flask run --host=0.0.0.0
 
