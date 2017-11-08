from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User
from datetime import datetime    
from django.core.validators import MinLengthValidator


class Food(models.Model):
	# foreign key to the user who owns it
	user = models.ForeignKey(User, default=1)
	movie_name=models.CharField(max_length=25)
	ticket_price=models.IntegerField(default=0)
	gener=models.CharField(max_length=10,default="abc")
	
	def __str__(self):
		return str(self.movie_name)

