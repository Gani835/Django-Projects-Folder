from django.db import models

# Create your models here.
class Amazonproducts(models.Model):
    prodId=models.IntegerField(primary_key=True)
    prodname=models.CharField(max_length=20)
    prodprice=models.IntegerField()
    prodimage=models.ImageField(upload_to='media/', null=True)
    
    class Meta:
        verbose_name_plural='Amazonproducts'
        
    def __str__(self):
        return self.prodname