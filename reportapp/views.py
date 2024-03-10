from django.shortcuts import render
from reportapp.models import Article
from django.utils import timezone
from .models import Article


def ReportLostItem(request):
   if request.method=='POST':
      name=request.POST.get('name')
      brand=request.POST.get('brand')
      category=request.POST.get('category')
      lostlocation=request.POST.get('lostlocation')
      lostdate=request.POST.get('lostdate')
      description=request.POST.get('description')
      
      
      try:
         Article.objects.create(
            name=name,
            brand = brand,
            category=category,
            lostlocation=lostlocation,
            lostdate=lostdate,
            description=description,    
         )
         print(brand, name,category,lostlocation)
      except:
         print('not created')
         pass
   print(' The lost item has been reported successfully.')
   return render(request, 'reportlost.html')

def ReportFoundItem(request):
   if request.method=='POST':
      name=request.POST.get('name')
      brand=request.POST.get('brand')
      category=request.POST.get('category')
      foundlocation=request.POST.get('foundlocation')
      founddate=request.POST.get('founddate')
      description=request.POST.get('description')
      
      
      try:
         Article.objects.create(
            name=name,
            brand = brand,
            category=category,
            foundlocation=foundlocation,
            founddate=founddate,
            description=description

            
         )
         print(brand, name,category,foundlocation)
      except:
         print('not created')
         pass
   print('The found item has been reported successfully.')
   
   return render(request, 'reportfound.html')



    
     