### A simple e-Commerce Webapp using Django [[1]](https://www.djangoproject.com/), Django REST framework [[2]](https://www.django-rest-framework.org/), PostgreSQL [[3]](https://www.postgresql.org/)

### Project Description
A simple e-Commerce website where sellers can post ads of their products and buyers can buy.

### TO DO & Implementations so far
- See [Issues](https://github.com/MuizZer07/ship-shop/issues) and [project workflow](https://github.com/MuizZer07/ship-shop/projects/1)

### Project Planning and Design (initially planned)
#### Simple Class Diagram

![Class Diagram](https://github.com/MuizZer07/ship-shop/blob/master/pics/ShipShopDiagram.png "Class Diagram")

#### Website Map
![Website Map](https://github.com/MuizZer07/ship-shop/blob/master/pics/WebsiteMap.png "Website Map")

### Screenshot
![Index Page](https://github.com/MuizZer07/ship-shop/blob/master/pics/shipshop.png "Index Page")

### Install & Run Project
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
- [6] [https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html](https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html)
- [7] [https://wsvincent.com/django-rest-framework-user-authentication-tutorial/](https://wsvincent.com/django-rest-framework-user-authentication-tutorial/)
