
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

        if not feedbackemail or not feedbacktext or not rating:
            error_message = "All fields are required."
            return render(request, 'feedback.html', {'error_message': error_message})

        try:
            feedback_instance = Feedback.objects.create(
                feedbackemail=feedbackemail,
                feedbacktext=feedbacktext,
                rate=rating
            )
            print(f"Feedback instance created: {feedback_instance}")
            
            success_message = "Feedback submitted successfully"
            return render(request, 'feedback.html', {'success_message': success_message})
        except Exception as e:
            print(f"Error creating feedback: {e}")

    return render(request, 'feedback.html')



