FROM python:3.11-slim

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi-py3 && \
    apt-get clean

WORKDIR /var/www/html/animages

COPY . /var/www/html/animages/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY animages.conf /etc/apache2/sites-available/

RUN a2ensite animages && a2enmod wsgi

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]