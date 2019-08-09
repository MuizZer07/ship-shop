### A simple e-Commerce Webapp using Django [[1]](https://www.djangoproject.com/), Django REST framework [[2]](https://www.django-rest-framework.org/), PostgreSQL [[3]](https://www.postgresql.org/)

#### Project Description
A simple e-Commerce website where sellers can post ads of their products and buyers can buy.

#### TO DO & Implementations so far
- See [Issues](https://github.com/MuizZer07/ship-shop/issues) and [project workflow](https://github.com/MuizZer07/ship-shop/projects/1)

#### Simple Class Diagram for the project

![Class Diagram](https://github.com/MuizZer07/ship-shop/blob/master/ShipShopDiagram.png "Class Diagram")

#### install modules
- ##### With Pipenv (it will install modules automatically)
Install Pipenv
```
$ pip install pipenv
```
Initiate pipenv shell and install modules
```
$ pipenv shell
$ pipenv install
```

- ##### Or install modules from requirement.txt
```
$ pip install -r requirements.txt
```

#### Run project
_*** Need to configure PostgreSQL Database in your PC. Tutorial Links: [[4]](https://www.youtube.com/watch?v=-LwI4HMR_Eg) & [[5]](https://www.youtube.com/watch?v=Axh8rNKgvmk)._

```
$ cd shipshop_django
$ python manage.py migrate
$ python manage.py runserver
```

*** To create and access admin privilege
```
$ python manage.py createsuperuser
```

### References
- [1] [https://www.djangoproject.com/](https://www.djangoproject.com/)
- [2] [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- [3] [https://www.postgresql.org/](https://www.postgresql.org/)
- [4] [https://www.youtube.com/watch?v=-LwI4HMR_Eg](https://www.youtube.com/watch?v=-LwI4HMR_Eg)
- [5] [https://www.youtube.com/watch?v=Axh8rNKgvmk](https://www.youtube.com/watch?v=Axh8rNKgvmk)
