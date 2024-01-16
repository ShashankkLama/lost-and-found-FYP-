from django.shortcuts import render

# Create your views here.
def ReportItemPage(request):
    return render(request, 'report.html')
    