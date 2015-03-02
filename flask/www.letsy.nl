server {
  server_name  letsy.nl;
  rewrite ^(.*) http://www.letsy.nl$1 permanent;
}

server {
  server_name www.letsy.nl;
  location / {
    include uwsgi_params;
    uwsgi_pass unix:/tmp/letsy.sock;
  }
  location static {
    alias /home/www/letsy/static;
  }
}
