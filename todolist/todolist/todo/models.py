from django.db import models
from django.conf import settings

from datetime import datetime
# Create your models here.


PRIORITY_CHOICES = ( 
  ('Low', 'Low'), 
  ('Normal', 'Normal'), 
  ('High', 'High'), 
) 
# PRIORITY_CHOICES = ( 
#   (1, 'Low'), 
#   (2, 'Normal'), 
#   (3, 'High'), 
# ) 
class Todo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=250)
	# priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
	priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, blank = False,null=False, default='Select') 
	text = models.TextField(default='default text here')
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	"""docstring for ClassName"""
	def __str__(self):
		return self.title
		