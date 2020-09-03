# python-PostgreSQL

## python dengan database sql PostgreSQL

* how to run

```

python manage.py runserver

```


* database postgreSQL console : 

```

create database python_postgresql_db;

```

* database config : 

```
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'python_postgresql_db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

```


* migrate model to database 

```

python manage.py migrate

```