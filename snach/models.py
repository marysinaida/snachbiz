from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=30, default = "")
    location = models.CharField(max_length=100, default="")
    product = models.CharField(max_length =50,default = "")
    phone_number = models.CharField(max_length=10,default="")

    def __str__(self):
        return self.name
    

class Products(models.Model):
    title = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    products_image = models.ImageField(upload_to = "image/")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,)


    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['title']


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
