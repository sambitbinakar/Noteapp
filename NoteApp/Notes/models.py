from django.db import models
from django.contrib.auth.models import User
# Create your models here.
catagory =(('Business','Business'),
          ('personal','persional'),
          ('important','important')) 

class Note(models.Model):
    title=models.CharField(max_length=200) 
    content = models.TextField()
    catagory = models.CharField(max_length=100,choices=catagory,default="personal")
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User ,on_delete=models.CASCADE,related_name='Notes' )

    def __str__(self):
        return self.title
