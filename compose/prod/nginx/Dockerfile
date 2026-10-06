FROM nginx:1.23-alpine

RUN rm /etc/nginx/nginx.conf
COPY main.conf /etc/nginx/nginx.conf

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY certs/vintagecell_co.crt /etc/nginx/ssl/
COPY certs/vintagecell_co.key /etc/nginx/ssl/
