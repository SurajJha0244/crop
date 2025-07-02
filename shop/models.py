from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=255)
    publish_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    

    
    def __str__(self):
        return self.product_name

class contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")
    
    def __str__(self):
        return self.name
    
# class Crop_Recommend(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
#     recommend_id=models.AutoField(primary_key=True)
#     nitrogen = models.FloatField(default=0.0)
#     phosphorus = models.FloatField(default=0.0)
#     potassium = models.FloatField(default=0.0)
#     temperature = models.FloatField(default=0.0)
#     humidity = models.FloatField(default=0.0)
#     ph = models.FloatField(default=0.0)
#     rainfall = models.FloatField(default=0.0)
#     predicted_crop = models.CharField(max_length=50 ,default='')
#     timestamp = models.DateTimeField(default=timezone.now)
    
#     def __str__(self):
#         return str(self.predicted_crop)
    
class crop_recommend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommend_id=models.AutoField(primary_key=True)
    nitrogen = models.FloatField(default=0.0)
    phosphorus = models.FloatField(default=0.0)
    potassium = models.FloatField(default=0.0)
    temperature = models.FloatField(default=0.0)
    humidity = models.FloatField(default=0.0)
    ph = models.FloatField(default=0.0)
    rainfall = models.FloatField(default=0.0)
    predicted_crop = models.CharField(max_length=50 ,default='')
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.predicted_crop)