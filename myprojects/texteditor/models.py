from django.db import models
#from django_quill.fields import QuillField
# Create your models here.

class another_model(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=100)
    animal=models.CharField(max_length=100)
    thing=models.CharField(max_length=100)
    #content=QuillField(blank=True)