from django.db import models
from sorl.thumbnail.fields import ImageField
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    # pieces = ...
    def __unicode__(self):
        return self.name


class Family(models.Model):
    last_name = models.CharField(max_length=255, blank=True, null=True,)
    footnote = models.CharField(max_length=255, blank=True, null=True,)
    story = models.TextField(blank=True, null=True,)
    sound = models.FileField(null=True, upload_to="zvuks", blank=True, )
    countries = models.ManyToManyField("Country", blank = True, null=True,)  
    def __unicode__(self):
        return self.prezime  


class Pic(models.Model):
    family=models.ForeignKey("Family", null=True, related_name="pics", blank=True)
    decade= models.IntegerField(null=True, blank=True)
    image=ImageField(null=True, upload_to="slike", blank=True)
    def __unicode__(self):
        return self.image



