FROM nginx

# remove default conf
RUN rm /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html

# don't name it default, ngix will create default index.html
COPY django.conf /etc/nginx/conf.d/django.conf