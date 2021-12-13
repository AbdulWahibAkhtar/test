FROM python:3.8-alpine

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/
ENV FLASK_APP app.py
ENV FLASK_ENV development
CMD flask run --host=0.0.0.0
COPY rootCA.pem /etc/nginx/ssl/
COPY site.crt /etc/nginx/ssl/
ssl_certificate = site.crt     
ssl_certificate_key = rootCA.pem 



