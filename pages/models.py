from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Media%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    
    def str(self):
        return self.title

class repair(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products1/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    
    def str(self):
        return self.title
    
    
class model(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products1/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def str(self):
        return self.title

class home1(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products1/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def str(self):
        return self.title
