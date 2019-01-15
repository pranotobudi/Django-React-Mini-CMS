from django.db import models
from django.db.models import CharField, TextField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title


class Article1(models.Model):
    title = CharField(max_length=30)
    content = TextField()

    def __str__(self):
        return self.title
    

from django.db import models 
from django.db.models import CharField, TextField 

class Article2(models.Model):
    title = CharField(max_length=30)
    content = TextField()
    def __ref__(self):
        return self.title

from django.db import models
from django.db.models import CharField, TextField 

class Article3(models.Model):
    title = CharField(max_length=30)
    content = TextField()

    def __str__(self):
        return self.title

from django.db import models 
from django.db.models import CharField, TextField  

class Article4(models.Model):
    title = CharField(max_length=30)
    content = TextField()

    def __str__(self):
        return self.title

from django.db import models 
from django.db.models import CharField, TextField 

