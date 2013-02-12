import os

from django.conf import settings
from django.db import models
from sorl.thumbnail.fields import ImageField




class Pic(models.Model):
    decade = models.IntegerField(blank=True, null=True)
    image = ImageField(upload_to=settings.MEDIA_ROOT)


    def __unicode__(self):
        return os.path.basename(self.image.name)


    def get_absolute_url(self):
        return "%s%s" % (settings.MEDIA_URL, self)




class Family(models.Model):
    last_name = models.CharField(max_length=255)
    footnote = models.CharField(max_length=255, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    sound = models.FileField(upload_to="zvuks", blank=True, null=True)
    pics = models.ManyToManyField(Pic, blank=True, null=True)


    def get_absolute_url(self):
        return "/family/%d" % self.id


    def __unicode__(self):
        return self.last_name


    class Meta:
        verbose_name_plural = "Families"




class Country(models.Model):
    name = models.CharField(max_length=255)
    family = models.ManyToManyField(Family, blank=True, null=True)


    def get_absolute_url(self):
        return "/country/%d" % self.id


    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Countries"



