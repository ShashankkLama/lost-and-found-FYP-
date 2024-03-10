from django.shortcuts import render
from .models import Feedback
from django.shortcuts import HttpResponse

def GiveFeedback(request):
    if request.method == 'POST':
        feedbackemail = request.POST.get('email')
        feedbacktext = request.POST.get('feedbacktext')
        rating = request.POST.get('rating')

        print(f"Feedback email: {feedbackemail}")
        print(f"Feedback text: {feedbacktext}")
        print(f"Rating: {rating}")

        try:
            feedback_instance = Feedback.objects.create(
                feedbackemail=feedbackemail,
                feedbacktext=feedbacktext,
                rate=rating
            )
            print(f"Feedback instance created: {feedback_instance}")
        except Exception as e:
            print(f"Error creating feedback: {e}")

    return render(request, 'feedback.html')


