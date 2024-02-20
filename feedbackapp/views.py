from django.shortcuts import render
from django.shortcuts import render
# from feedbackapp.models import Feedback

# Create your views here.

def GiveFeedback(request):
    
    return render(request, 'feedback.html')
    