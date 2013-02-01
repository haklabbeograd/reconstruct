from django.db import models


class Family(models.Model):
	surname = models.CharField(max_length=100)

	def __unicode__(self):
		return self.surname


	class Meta:
		verbose_name_plural = 'Families'
