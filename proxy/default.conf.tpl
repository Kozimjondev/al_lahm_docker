server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }

    location / {
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        uwsgi_pass             ${APP_HOST}:${APP_PORT};
        include                /etc/nginx/uwsgi_params;
        client_max_body_size   50M;
    }
    
}