from django.db import models

# Create your models here.
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class picDataSet(models.Model):
    dataName = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    dataNum = models.IntegerField(default=0)
    def __str__(self):
        return self.dataName


class picData(models.Model):
    setSource = models.ForeignKey(picDataSet,on_delete=models.DO_NOTHING)
    log = models.DecimalField(default=0.0,max_digits=8, decimal_places=3)
    lat = models.DecimalField(default=0.0,max_digits=8, decimal_places=3)
    typeData = models.TextField()
    wordData = models.TextField()