#!/usr/bin/env python3
#script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
        </html>" | sudo tee /data/web_static/releases/test/index.html

sudo mkdir /data/web_static/shared/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '23i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
