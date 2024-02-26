from django.shortcuts import render
from django.shortcuts import render
from .models import Feedback
from django.shortcuts import HttpResponse


def GiveFeedback(request):
    if request.method == 'POST':  
        feedbackemail = request.POST.get('emailinput')
        feedbacktext = request.POST.get('experiencetext')
        # rate= request.POST.get(rate)
        
        try:
            Feedback.objects.create(
                feedbackemail=feedbackemail,
                feedbacktext=feedbacktext,
            )  
            
            
        except:
         print('not created')
         pass
  
        print(feedbacktext, feedbackemail)
    
    return render(request, 'feedback.html')
    