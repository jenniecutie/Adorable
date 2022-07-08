from django.shortcuts import render, redirect
from .models import *

def MainPage(request):
   return render(request, 'Mainpage.html')

def recipe(request):
   return render(request, 'Recipe.html')

def buchii(request):
   return render(request, 'buchi.html')

def buchii1(request):
   return render(request, 'buchi1.html')

def buchii2(request):
   return render(request, 'buchi2.html')

def bibingkaaa(request):
   return render(request, 'bibingka.html')

def bibingkaa1(request):
   return render(request, 'bibingka1.html')

def bibingkaa2(request):
   return render(request, 'bibingka2.html')

def sansrivalll(request):
   return render(request, 'sansrival.html')

def sansrivalll1(request):
   return render(request, 'sansrival1.html')

def sansrivalll2(request):
   return render(request, 'sansrival2.html')

def pichiiii(request):
   return render(request, 'pichi.html')

def pichiii1(request):
   return render(request, 'pichi1.html')

def pichiii2(request):
   return render(request, 'pichi2.html')

def putooo(request):
   return render(request, 'puto.html')

def putooo1(request):
   return render(request, 'puto1.html')

def putooo2(request):
   return render(request, 'puto2.html')

def tahooo(request):
   return render(request, 'taho.html')

def tahooo1(request):
   return render(request, 'taho1.html')

def tahooo2(request):
   return render(request, 'taho2.html')

def turonnn(request):
   return render(request, 'turon.html')

def turonnn1(request):
   return render(request, 'turon1.html')

def turonnn2(request):
   return render(request, 'turon2.html')

def bananaaa(request):
   return render(request, 'banana.html')

def bananaaa1(request):
   return render(request, 'banana1.html')

def bananaaa2(request):
   return render(request, 'banana2.html')

def halohalooo(request):
   return render(request, 'halo.html')

def halohalooo1(request):
   return render(request, 'halo1.html')

def halohalooo2(request):
   return render(request, 'halo2.html')

def lecheflannn(request):
   return render(request, 'leche.html')

def lecheflannn1(request):
   return render(request, 'leche1.html')

def lecheflannn2(request):
   return render(request, 'leche2.html')

def aboutUs(request):
   
   return render(request, 'AboutUs.html')

def personalInfoForm(request):

   if request.method == "POST":
      person_info = PersonalInfoNiUser.objects.create(
         fullName = request.POST['fullName'],
         mobileNo = request.POST['mobileNo'],
         emailAdd = request.POST['emailAdd'],
         streetAdd = request.POST['streetAdd'],
         barangay  = request.POST['barangay'],
         municipal = request.POST['municipal'],
         province  = request.POST['province'],)
      person_info.save()
      return redirect(f'/index2/{person_info.id}/')
   else:
      return render(request, 'index.html')

def dessertInfoForm(request, person_id):
   person_info = PersonalInfoNiUser.objects.get(id=person_id)

   if request.method == "POST":
      dessertinfo = Submitted_Recipe.objects.create(
         dName = request.POST['dessertName'],
         dDescription = request.POST['description'],
         dPrepTime = request.POST['prepTime'],
         dCookTime = request.POST['cookTime'],
         dYieldServing = request.POST['yieldServing']
         )
      dessertinfo.save()
      return redirect(f'/index3/{person_info.id}/{dessertinfo.id}/')
   else:
      return render(request, 'index2.html')

def ingredients(request,person_id, dessert_id):

   person_info = PersonalInfoNiUser.objects.get(id=person_id)
   dessertinfo = Submitted_Recipe.objects.get(id=dessert_id)

   if request.method == "POST":

      ingredients = Ingredients_Used.objects.create(
         ingredientsName = request.POST['form[]'])

      ingredients.save()
      return redirect(f'/index4/{person_info.id}/{dessertinfo.id}/{ingredients.id}/')
   else:
      return render(request, 'index3.html')

def directiontoCookForm(request, person_id, 
   dessert_id, ingredients_id):

   person_info = PersonalInfoNiUser.objects.get(id=person_id)
   dessertinfo = Submitted_Recipe.objects.get(id=dessert_id)
   ingredientss = Ingredients_Used.objects.get(id=ingredients_id)

   if request.method == "POST":
      direction_cook = Procedure_of_Recipe.objects.create(direction=request.POST['form[]'])
      direction_cook.save()

      dessertlist = DessertList.objects.create(person = person_info,
         recipe = dessertinfo,
         direction = direction_cook,
         ingredients = ingredientss,
         )
      dessertlist.save()
      return redirect(f'/tableshowform/{person_info.id}/')

   else:
      return render(request, 'index4.html')

def tableShowForm(request, person_id):
   person_info = PersonalInfoNiUser.objects.get(pk=person_id)
   dessert = DessertList.objects.filter(person=person_info)


   if request.method == "POST":
      return redirect(f'/index2/{person_info.id}/')

   return render(request, 'tableshow.html',{'desserts':dessert, 'person':person_info})

def delete(request, person_id,item_id):
   person = PersonalInfoNiUser.objects.get(pk=person_id)
   item = DessertList.objects.get(id=item_id)
   item.delete()
   return redirect(f'/tableshowform/{person.id}/')