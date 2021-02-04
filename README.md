# datalink

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
   11  python datalink.py 
   12  git pull https://github.com/FYDP-SmartPantry/datalink.git
   13  python datalink.py 
   14  pip install gunicorn
   15  python datalink.py 
   16  vim datalink.py 
   17  python datalink.py 
   18  touch wsgi.py
   19  vim wsgi.py 
   20  gunicorn --bind 0.0.0.0:5000 wsgi:app
   21  deactivate
   22  vim /etc/systemd/system/myproject.service
   23  sudo vim /etc/systemd/system/datalink.service
   24  ls -a /etc/systemd/system/
   25  pwd
   26  sudo vim /etc/systemd/system/datalink.service
   27  sudo systemctl start datalink
   28  sudo systemctl enable datalink
   29  sudo systemctl status datalink
   30  sudo vim /etc/nginx/sites-available/datalink
   31  sudo apt update
   32  sudo apt install nginx
   33  sudo ufw app list
   34  sudo ufw allow 'Nginx HTTP'
   35  sudo ufw status
   36  sudo ufw allow 'Nginx HTTP'
   37  sudo ufw status
   38  systemctl status nginx
   39  cd /etc
   40  cd nginx/
   41  cd sites-available/
   42  ls
   43  vim datalink
   44  sudo vim datalink
   45  cd
   46  cd datalink/
   47  pwd
   48  cd /etc/nginx/sites-available/
   49  vim datalink 
   50  sudo vim datalink 
   51  clear
   52  sudo ln -s /etc/nginx/sites-available/datalink /etc/nginx/sites-enabled/
   53  sudo nginx -t
   54  sudo systemctl restart nginx
   55  sudo ufw delete allow 5000
   56  sudo ufw allow 'Nginx Full'
   57  sudo systemctl stauts nginx
   58  sudo systemctl status nginx
   59  cd
   60  cd datalink/
   61  ls
   62  cd
   63  clear
   64  sudo vim /etc/nginx/sites-available/datalink 
   65  sudo ln -s /etc/nginx/sites-available/datalink /etc/nginx/sites-enabled/
   66  rm -rf /etc/nginx/sites-enabled/*
   67  sudo rm -rf /etc/nginx/sites-enabled/*
   68  sudo ln -s /etc/nginx/sites-available/datalink /etc/nginx/sites-enabled/
   69  sudo systemctl restart nginx
   70  sudo ufw allow 5000
   71  sudo systemctl status nginx
   72  cd datalink/
   73  ls
   74  vim datalink.py 
   75  sudo systemctl restart nginx
   76  sudo systemctl restart datalink
   77  sudo systemctl status datalink
   78  sudo systemctl restart nginx
   79  cat datalink.py 
   80  history | tail -n 100
