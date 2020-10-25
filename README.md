# BadgeProject

steps to setup localenvironment

1. sudo apt install pipenv
2. pipenv install --skip-lock
3. pipenv install django
4. pipenv shell
5. pipenv lock
6. django-admin.py startproject BadgeProject .
7. python manage.py migrate
8. python manage.py runserver

Open the link in browser. You succeeded in creating local setup.

9. activate venv by
$ source //home/<your system username>/.local/share/virtualenvs/Badging_system_krunal-Qbp0rnPl/bin/activate
eg.

$ source //home/kp-ubuntu/.local/share/virtualenvs/Badging_system_krunal-Qbp0rnPl/bin/activate

10. git init (install git)
11. git status
12. git add .
13. git commit -m "msg"
14. git remote add <reponame> <repo url>
Eg. git remote add Badging_system_krunal https://github.com/gitkp11/Badging_system_krunal.git
