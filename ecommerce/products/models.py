from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# CATAGORY_CHOICES = (
#   ('Electronics', 'Electronics'),
#   ('Clothing', 'Clothing'),
#   ('Technology', 'Technology'),
 
  
#   ('Sports', 'Sports'),
#   ('Health', 'Health'),
# )
#creating out own catagory
class Catagory(models.Model):
  name = models.CharField(max_length=10)
  def __str__(self):
    return self.name
class Product(models.Model):
  name = models.CharField(max_length=10)
  description = models.TextField(max_length=50)
  catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,related_name ='products')
  price = models.DecimalField(max_digits=8, decimal_places=2)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='products')
  created = models.DateTimeField(auto_now=True)
  update = models.DateTimeField(auto_now_add=True)
