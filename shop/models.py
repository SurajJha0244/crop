from django.db import models

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
    
class Crop_Recommend(models.Model):
    recommend_id=models.AutoField(primary_key=True)
    Nitrogen=models.FloatField()
    Phosphorus=models.FloatField()
    Potassium=models.FloatField()
    Rainfall=models.FloatField()
    pH = models.FloatField()
    temperature=models.FloatField(default=0.0)
    humidity=models.FloatField(default=0.0)
    
    def __str__(self):
        return str(self.recommend_id)