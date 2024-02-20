from django.urls import path
from feedbackapp import views


urlpatterns = [
    path('feedback', views.GiveFeedback, name='feedback'),
]
