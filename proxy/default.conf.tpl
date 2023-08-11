upstream django{
    server django_app:8001
}

server {
    listen ${LISTEN_PORT};
    proxy_force_ranges on;
    max_ranges 100;
    add_header Accept-Ranges bytes;

    location /static {
        alias /vol/static;
    }

    location / {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_ignore_client_abort on;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
        uwsgi_pass             ${APP_HOST}:${APP_PORT};
        include                /etc/nginx/uwsgi_params;
        client_max_body_size   50M;
    }
    
}