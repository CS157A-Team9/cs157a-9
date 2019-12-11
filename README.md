# cs157a-9
CS157A Team #9 project

## Table of Contents
- [Project Final Report](#project-final-report)
- [Project Proposal](#project-proposal)
- [Project Requirements](#project-requirements)
- [Development Guide](#development-guide)
  * [System Dependencies](#system-dependencies)
  * [Installation (Mac)](#installation-mac)
    + [Homebrew](#homebrew)
    + [Python 3](#python-3)
    + [Pipenv](#pipenv)
  * [Getting Started](#getting-started)
    + [MySQL](#mysql)
    + [Django](#django)
    + [Django Admin](#django-admin)
  * [Django with Apache](#django-with-apache)
    + [Mac](#mac)
      - [Install mod_wsgi](#install-mod_wsgi)
      - [Configure Apache](#configure-apache)
- [Running In Production](#running-in-production)
  * [Notes](#notes)
  
## Project Final Report
https://docs.google.com/document/d/1kSahJwNKnsgM09UmhIaYCjC4EbMnRh2AjFMQwW1U9N0/edit?usp=sharing

## Project Proposal
https://docs.google.com/document/d/1cPT1TBGzdlqpoYTMWRF7JZ2daHiAtQl9f8OHPTmBvnM/edit?usp=sharing

## Project Requirements
https://docs.google.com/document/d/1ilFfwDIK17xxILQx0scwFLeDIWO_rgJXE4wsyqgTEao/edit?usp=sharing

# Development Guide

## System Dependencies
| Name   | Version |
|--------|---------|
| Apache | *       |
| MySQL  | 8       |
| Python | 3       |
| Pipenv | *       |

\* No specific version requirement

## Installation (Mac)

### Homebrew
Homebrew is a package manager for Mac which will be used to install the necessary software for this project.

Ensure command line tools are installed by running the following in your terminal
```
--xcode-select --install
```

Run the following to install Homebrew on your system
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Python 3
Install python 3 via Homebrew
```
brew install python
```

### Pipenv
Pipenv helps to manage the python virtual environment as well as python dependencies.
Install via Homebrew
```
brew install pipenv
```

## Getting Started
Once all system dependencies have been installed, install python dependencies with pipenv
```
pipenv install
```

To activate the virtual environment run `pipenv shell` from the command line. You can exit the shell with `exit`. Once in the shell, the django commands can be readily accessed.

### MySQL
In order to give Django access to the MySQL database, we need to create a user and grant appropriate privileges. Log in to your MySQL database from the terminal and run the following
```
CREATE USER django@localhost IDENTIFIED BY 'team99*';
CREATE DATABASE team9;
GRANT ALL ON team9.* TO django@localhost;
```

To import timezones into MySQL, run the following in your terminal
```
mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -D mysql --user=root -p
```

### Django
Now that Django has access to the MySQL database, we can run migrations to populate the database with default tables. Make sure you have activated the python virtual environment before running the following commands (i.e. in the Pipenv shell)
```
./manage.py migrate
```
**Note:** You will need to run migrations periodically to sync Django models to the database.

To start the Django development server, run the following
```
./manage.py runserver
```

Then visit http://localhost:8000 in your browser.

### Django Admin
Django comes with a built in admin panel that can be accessed via http://localhost:8000/admin. In order to login, a user needs to be created first. To create a super user, use the following command from the terminal
```
./manage.py createsuperuser
```

## Django with Apache
### Mac
To use Apache as the server to deploy the Django application, follow the steps below.
#### Install mod_wsgi
https://pypi.org/project/mod-wsgi/
#### Configure Apache
Use terminal and type the following:
```
sudo -s
cd /etc/apache2
```
Add the configuration for the Django application by modifying apache2 httpd.conf file.
```
vim httpd.conf
```
This command will open the httpd.conf file and allow text edit in terminal. Modify the following lines according to your local path and add them to the httpd.conf file.
```
LoadModule wsgi_module /Users/YOUR_USER_NAME/.local/share/virtualenvs/cs157a-9-wSNcz8AY/lib/python3.7/site-packages/mod_wsgi/server/mod_wsgi-py37.cpython-37m-darwin.so
WSGIScriptAlias / /Users/YOUR_USER_NAME/cs157a-9/team9/team9/wsgi.py
WSGIPythonHome /Users/YOUR_USER_NAME/.local/share/virtualenvs/cs157a-9-wSNcz8AY
WSGIPythonPath /Users/YOUR_USER_NAME/cs157a-9/team9

<Directory /Users/YOUR_USER_NAME/cs157a-9/team9/team9>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
```
**Note:** 
LoadModule wsgi_module (path_to_your_mod_wsgi.so)
WSGIScriptAlias / (path_to_your_project_folder_containing_wsgi.py)
WSGIPythonHome (path_to_your_pipenv_for_the_project)
WSGIPythonPath (path_to_your_project_folder)

To find out location of the python development environment for the project, do the following:
```
pipenv shell
cd your_project_path
```
run
```
python -c 'import sys; print(sys.prefix)'
```
A directory will be displayed on your console and that would be the path to the pipenv.


After adding the configurations to httpd.conf, exit text editing mode by
```
Press Esc to escape insert mode
Then type :wq!
```
Remember to restart the Apache server to reflect changes
```
sudo apachectl restart
```

If successful, the default Django page will be displayed when accessing 
```
localhost
or
http://127.0.0.1/
```

# Running In Production

## Notes
We have chosen to use the pure python adapter for mysql (mysql-connector-python) even though it is less efficient than the alternatives due to some known issues getting Python and MySQL to play well together in a Mac environment. When running the app in production, it will be very advantages in terms of performance to use mysqlclient instead.
