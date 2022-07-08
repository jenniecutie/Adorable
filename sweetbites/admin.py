from django.contrib import admin
from .models import *
admin.site.register([PersonalInfoNiUser, Submitted_Recipe, 
	Procedure_of_Recipe, DessertList, Ingredients_Used])
