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
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    available_quantity = models.IntegerField()
    price = models.FloatField(blank=True)
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

class Order(models.Model):
    '''
        order model to store all orders
    '''

    id = models.AutoField(primary_key=True)
    order_key = models.CharField(max_length=8)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)
    total = models.FloatField()
    products = models.ManyToManyField(Product)
    quantity_list = models.CharField(max_length=80, null=True)

    STATUS = [
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    ]

    status = models.CharField(
        choices=STATUS,
        max_length=50,
        default='Pending'
    )

    def __str__(self):
        return self.name
