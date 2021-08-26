#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "
<html>
  <head>
    <meta charset='UTF-8'>
    <title>My profile</title>
  </head>
  <body>
    <a href="https://github.com/Frank-Grijalba">My Github</a>
    <br><a href="https://twitter.com/FrankGrijalba">My twitter</a></br>
  </body>
</html>
" >> /data/web_static/releases/test/index.html

sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R "$USER":"$USER" /data/
sudo sed -i '/listen 80 default_server/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
