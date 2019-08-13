from django.db import models
from users.models import User

'''
    model classes
'''

class Product(models.Model):
    '''
        product model to store product information
    '''

    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    available_quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True)

    categories = [
        ('Entertainment', 'Entertainment'),
        ('Computer & Accessories', 'Computer & Accessories'),
        ('Mobile & Accessories', 'Mobile & Accessories'),
        ('Clothings', 'Clothings'),
        ('Electronics', 'Electronics'),
        ('Health & Beauty', 'Computer & Accessories'),
        ('Home & Lifestyle', 'Mobile & Accessories'),
        ('Sport', 'Sport'),
        ('Men\'s Fashion', 'Men\'s Fashion'),
        ('Women\'s Fashion', 'Women\'s Fashion'),
        ('Others', 'Others'),
    ]

    category = models.CharField(
        choices=categories,
        max_length=50,
        default='Others'
    )

    def __str__(self):
        return self.name
