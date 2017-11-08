# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Food
# Create your views here.

def index(request):
	all_food_items=Food.objects.all()
	context={'food_items':all_food_items}
	return render(request,'Food/index.html',context)
	