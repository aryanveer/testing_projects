from django.db import models
from django.contrib.auth.models import Group

# Create your models here.


class Keywords(models.Model):

	class Meta:
		db_table = "keywords"

	group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
	keyword = models.CharField(max_length=200, null=False, blank=False, unique=True)
	source = models.CharField(max_length=200, null=False, blank=False)
	priority = models.IntegerField(default=0)
	similar_keywords = models.CharField(max_length=1000, blank=True)

	def __str__(self):
		return self.keyword
