from django.conf import settings
from django.db import models
from sorl.thumbnail.fields import ImageField



class Country(models.Model):
    name = models.CharField(max_length=255)


    def __unicode__(self):
        return self.name



class Family(models.Model):
    last_name = models.CharField(max_length=255)
    footnote = models.CharField(max_length=255, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    sound = models.FileField(upload_to="zvuks", blank=True, null=True)
    countries = models.ManyToManyField(Country, blank=True, null=True)


    def get_absolute_url(self):
        return "/family/%d" % self.id


    def __unicode__(self):
        return self.last_name



class Pic(models.Model):
    family = models.ForeignKey(Family, related_name="pics", blank=True, null=True)
    decade = models.IntegerField(blank=True, null=True)
    image = ImageField(upload_to="slike", blank=True, null=True)


    def __unicode__(self):
        return self.image.url
