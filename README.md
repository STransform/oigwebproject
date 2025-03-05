
##Oromia Investment Group 

## Brief Description**

This dynamic web-based system is developed for Oromia Investment Group 

# Technology Stack

The following are the core technologies used to build the application.

* Back-end: Django (a Python web framework)
* Front-end: HTML, CSS, JavaScript, Bootstrap (web development technologies)
* Database:MySQL


# Prerequisites and Dependencies
    Operating System: System has been tested on Windows 11 and linux operating system. Since the project is developed using Django
    and it's dependencies theoretically it should be running in all operating systems including windows, linux

    Python version >= 3.8: Ensure you have the required Python version installed on your system. You can check the version by running `python --version` in your terminal.
    
    Other dependencies: All additional libraries required for the project are listed in the `requirements.txt` file and will be installed in following steps.


# Getting Started 

Follow the following steps to set up the development environment for your project.    

 ## Cloning the Repository to your local machine:
    * Use the provided command to download the project's codebase from GitHub.
    
    ```bash
    git clone https://github.com/STransform/oigwebproject.git
    ```

 ## Setting Up the Environment

    ## Create a virtual environment
        * This step isolates project dependencies from your system-wide Python installations.
        ```bash
        $ python -m venv venv
        ```
    ## Activate the virtual environment
        ```bash
        $ Scripts/activate
        ```

## Install dependencies
    
    This command installs all the required libraries listed in `requirements.txt` into your activated virtual environment.
    ```bash
        $ pip install -r requirements.txt
    ```
# Running the Project 

This section explains how to launch the development server and access your application locally.

## Database Migrations
    * These commands are essential for creating the database schema based on your project's models.
        * `makemigrations`: Analyzes your models and generates migration files.
       
        ``` bash
        $ python manage.py makemigrations about_us accounts blogs news core dashboard
        ```

        * `migrate`: Applies the generated migrations to your database.
        ``` bash
        $ python manage.py migrate
        ```
    
    ## Notes:
    * You can remove all the data from the databases and return to an empty state using the:
    ```bash
    $ python manage.py flush
    ```

    * The default database is Sqlite3 which will be generated when you run migration commands. You can configure any relational database supported by Django which includes PostgreSQL and MySQL. 
    Configuration of PostgreSQL:
    - Open the settings.py file inside the otech directory and replace the default database setting for Sqlite with the following PostgreSQL conf replacing your database credentials
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': $Your_DB_Name,
        'USER': $Your_DB_Username,
        'PASSWORD': $Your_DB_Password,
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
    For further reading on how to install MySql and integrate with Django use the following blog.
    
    
    Configuration of MySQL, 
    - Open the settings.py file and replace the default database setting for Sqlite with the following MySQL conf replacing your database credentials
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        ' NAME': $DB_Name,
        'USER': $DB_Username,
        'PASSWORD': $DB_Password,
        'HOST':'localhost',
        'PORT':'3306',
    }

##  To create a superuser account, use this command and fill in the required fields:

```bash
$ python manage.py createsuperuser
```

## Starting the Development Server
    * Run this command to launch the built-in Django development server.
    ```bash
    $ python manage.py runserver
    ```
## Access the application
    * You can then access your application by opening http://127.0.0.1:8000/ in your web browser.
    * Access website : http://127.0.0.1:8000/

    Login page url:
    http://127.0.0.1:8000/accounts/login/

    After Login
    * Access for internal dashboard
    http://127.0.0.1:8000/dashboard/

    * Access for admin
    http://127.0.0.1:8000/dashboard/


# Deployment:
The web app can be deployed on any hosting platform that supports Python. These Linux and Windows. Deployment instructions can have some specific differences based on the deployment platform. 

# Branching:
As a git repo, My repo will follow the common branching strategies. This is   main branch


* By Simon Temesgen(S-Transform)
  
"A passionate developer skilled in Java programming, with numerous projects completed using Java technologies and MySQL databases. 
Additionally, I develop projects using Django, the Python web framework, due to its simplicity."


