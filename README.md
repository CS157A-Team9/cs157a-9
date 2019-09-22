# cs157a-9
CS157A Team #9 project

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

## Django with Apache
### Mac
To use Apache as the server to deploy the Django application, follow the steps below.
#### Install mod_wsgi
https://pypi.org/project/mod-wsgi/
#### Configure Apache
Will Update
```
Include /private/etc/apache2/other/*.conf

LoadModule wsgi_module /Users/Ashley/.local/share/virtualenvs/cs157a-9-wSNcz8AY/lib/python3.7/site-packages/mod_wsgi/server/mod_wsgi-py37.cpython-37m-darwin.so
WSGIScriptAlias / /Users/Ashley/cs157a-9/team9/team9/wsgi.py
WSGIPythonHome /Users/Ashley/.local/share/virtualenvs/cs157a-9-wSNcz8AY
WSGIPythonPath /Users/Ashley/cs157a-9/team9
#WSGIPythonPath /Users/Ashley/.local/share/virtualenvs/cs157a-9-wSNcz8AY/lib/python3.7/site-packages

<Directory /Users/Ashley/cs157a-9/team9/team9>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
```

