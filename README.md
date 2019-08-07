### A simple e-Commerce App using Django, Django REST framework, PostgreSQL

#### Project Description
A simple e-Commerce website where sellers can post ads of their products and buyers can buy.

#### TO DO & Implementations so far
- See Issues section 

#### Simple Class Diagram for the project

![Class Diagram](https://github.com/MuizZer07/ship-shop/ShipShop Diagram.png "Class Diagram")

#### install modules
- ##### With Pipenv (it will install modules automatically)
```
$ pipenv shell
$ pipenv install
```

- ##### Or install modules from requirement.txt
```
$ pip install -r requirements.txt
```

#### Run project
*** Need to configure PostgreSQL Database in your PC
```
$ cd shipshop-django
$ python manage.py migrate
$ python manage.py runserver
```

*** To create and access admin privilege
```
$ python manage.py createsuperuser
```
