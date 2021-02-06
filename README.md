# datalink
```
   1  sudo apt update
    2  sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
    3  sudo apt install python3-venv
    4  git clone https://github.com/FYDP-SmartPantry/datalink.git
    5  cd datalink/
    6  python3.6 -m venv datalinkenv
    7  source datalinkenv/bin/activate
    8  pip install wheel
    9  pip install uwsgi flask
   10  sudo ufw allow 5000

   14  pip install gunicorn

   20  gunicorn --bind 0.0.0.0:5000 wsgi:app
   21  deactivate
  
   26  sudo vim /etc/systemd/system/datalink.service
   27  sudo systemctl start datalink
   28  sudo systemctl enable datalink
   29  sudo systemctl status datalink

   31  sudo apt update
   32  sudo apt install nginx
   33  sudo ufw app list
   34  sudo ufw allow 'Nginx HTTP'
   35  sudo ufw status

   38  systemctl status nginx

   48  cd /etc/nginx/sites-available/
   50  sudo vim datalink 

   52  sudo ln -s /etc/nginx/sites-available/datalink /etc/nginx/sites-enabled/
   53  sudo nginx -t
   54  sudo systemctl restart nginx

   56  sudo ufw allow 'Nginx Full'
   58  sudo systemctl status nginx

   80  history | tail -n 100
```
