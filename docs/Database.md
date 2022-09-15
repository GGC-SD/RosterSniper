# About the Database

Django has a built-in ORM that lets you create, retrieve, update and delete information from a relational database (Postgres, MySQL, SQLite etc) using Python instead of SQL. Tables are defined as python classes called *models* and the individual columns are defined as class instance variables called *fields*. The python classes and database tables are kept in sync through migrations. Basically, Django reads all of the model files and generates migration files which are placed in the app's `migrations` folder. This is done using the following command:
```sh
$ ./manage.py makemigrations
```
These migration files are typically stored in git. That way, only the developer that adds or updates a model needs to make the migration file and the other developers use the following command to execute it:
```sh
$ ./manage.py migrate
```
Here, Django uses the migration files to generate and run SQL that creates or modifies the database tables (the exact SQL is specific to your particular database). To see the SQL that a migration file will run, use the following command:
```sh
$ ./manage.py sqlmigrate app_label migration_name
```
NOTE: The app's internal label is "core" and the migrations are listed under ".\django_project\core\migrations" with 0001_initial being the thing you should call to set-up the tables and rows for a localhost database.

## Managing Data

Other commands that may come in handy are `dumpdata`, `loaddata`, and `flush` (documented [here](https://docs.djangoproject.com/en/stable/ref/django-admin/)). E.g.
```sh
$ ./manage.py dumpdata [app_label] --indent=4 -o data.json
$ ./manage.py flush
$ ./manage.py loaddata data.json
```

You can also use the Django [shell](https://docs.djangoproject.com/en/stable/ref/django-admin/#shell) to delete data from a particular model, e.g.
```py
from core.models import Model
Model.objects.all().delete()
```

## Superusers

Admins are users that can access the Django admin page `/admin/`. They can be created using the command
```sh
$ ./manage.py createsuperuser
```
which prompts you for an email and password.

To turn a preexisting user into an admin, using the Django shell, run
```py
from users.models import User
User.objects.filter(email='example@email.com').update(is_staff=True, is_superuser=True)
```
