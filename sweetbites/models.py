from django.db import models

class PersonalInfoNiUser(models.Model):
	fullName = models.CharField(max_length = 50)
	mobileNo = models.CharField(max_length = 11)
	emailAdd = models.CharField(max_length = 200)
	streetAdd = models.CharField(max_length = 50)
	barangay = models.CharField(max_length = 50)
	municipal = models.CharField(max_length = 50)
	province = models.CharField(max_length = 50)

class Submitted_Recipe(models.Model):
	dName = models.CharField(max_length = 100)
	dDescription = models.TextField(max_length = 500)
	dPrepTime = models.CharField(max_length = 500)
	dCookTime = models.CharField(max_length = 500)
	dYieldServing = models.IntegerField()
	

class Procedure_of_Recipe(models.Model):
	direction = models.CharField(max_length = 1000)

class Ingredients_Used(models.Model):
	ingredientsName = models.CharField(max_length = 50)


class DessertList(models.Model):
	person = models.ForeignKey(PersonalInfoNiUser, on_delete = models.CASCADE)
	recipe = models.ForeignKey(Submitted_Recipe, on_delete = models.CASCADE)
	direction = models.ForeignKey(Procedure_of_Recipe, on_delete = models.CASCADE)
	ingredients = models.ForeignKey(Ingredients_Used, on_delete = models.CASCADE)