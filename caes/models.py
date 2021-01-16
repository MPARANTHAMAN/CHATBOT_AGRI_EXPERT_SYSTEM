from django.db import models
from django.contrib.auth.models import User
class user_type(models.Model):
     name = models.CharField('User Type', max_length=120)
      
def __str__(self):
       return self.name

class home(models.Model):
    chat = models.CharField(max_length=255)
    
def __unicode__(self):
            return self.chat
