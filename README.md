# BadgeProject

## steps to setup localenvironment\

1. git clone https://github.com/gitkp11/BadgeProject.git
2. cd BadgeProject


**Virtualenv modules installation (Unix based systems)**\

3. virtualenv myenv
4. source myenv/bin/activate

**Virtualenv modules installation (Windows based systems)**\

3. virtualenv myenv
4. .\myenv\Scripts\activate

**Install modules**

5. pip3 install -r requirements.txt

**Create tables**

6. python manage.py makemigrations
7. python manage.py migrate

**Start the application (development mode)**

8. python manage.py runserver # default port 8000

**Start the app - custom port**

9. python manage.py runserver 0.0.0.0:<your_port>

**access the web app in browser:**

10. http://127.0.0.1:8000/


## GIT initialisation

1. git init (install git)
2. git status
3. git add .
4. git commit -m "msg"
5. git remote add <reponame> <repo url>
Eg. git remote add Badging_system_krunal https://github.com/gitkp11/Badging_system_krunal.git



## update requirements.txt
1. pip freeze > requirements.txt

## SET UP ENVIRONMENT VARIABLE IN UBUNTU
1. sudo gedit /etc/environment
paste your environement variable here
eg. EMAIL_HOST_USER="sureshmumbai2017@gmail.com"
2. source /etc/environment
3. gedit ~/.profile
paste your environement variable here
eg. export EMAIL_HOST_USER="sureshmumbai2017@gmail.com"
4. source ~/.profile
5. sudo gedit /etc/profile
paste your environement variable here
eg. export EMAIL_HOST_USER="sureshmumbai2017@gmail.com"
6. source /etc/profile
7. sudo gedit ~/.bashrc
paste your environement variable here
eg. export EMAIL_HOST_USER="sureshmumbai2017@gmail.com"
8. source ~/.bashrc


## deploy app on pythonanywhere
