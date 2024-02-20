from django.shortcuts import render
from reportapp.models import Article
from django.utils import timezone


def ReportItemPage(request):
   if request.method=='POST':
      name=request.POST.get('name')
      brand=request.POST.get('brand')
      category=request.POST.get('category')
      lostlocation=request.POST.get('lostlocation')
      foundlocation=request.POST.get('foundlocation')
      lostdate=request.POST.get('lostdate')
      founddate=request.POST.get('founddate')
      description=request.POST.get('description')
      
      try:
         Article.objects.create(
            name=name,
            brand = brand,
            category=category,
            lostlocation=lostlocation,
            foundlocation=foundlocation,
            lostdate=lostdate,
            founddate=founddate,
            description=description

            
         )
         print(brand, name,category,lostlocation)
      except:
         print('not created')
         pass
   print(' created')
   return render(request, 'report.html')

    
     