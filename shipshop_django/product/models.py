from django.db import models

'''
    model classes
'''

class Category(models.Model):
    '''
        category for each products
    '''

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    '''
        product model to store product information
    '''

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    available_quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
