from django.shortcuts import render
from .models import Article

# Create your views here.
def ReportItemPage(request):
     if request.method=='POST':
        name=request.POST.get('itemname')
        brand=request.POST.get('brand')
        category=request.POST.get('category')
        lostlocation=request.POST.get('lostlocation')
        foundlocation=request.POST.get('foundlocation')
        lostdate=request.POST.get('lostdate')
        founddate=request.POST.get('founddate')
        description=request.POST.get('description')

     return render(request, 'report.html')
    
    