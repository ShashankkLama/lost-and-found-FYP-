from django.urls import path
from feedbackapp import views
from django.contrib import admin
# from reportapp import views





urlpatterns = [
    path('feedback', views.GiveFeedback, name='feedback'),
    path('admin/', admin.site.urls),
    # path('feedback/', feedback_form, name='feedback_form'),
    # path('datashow', views.ReportFoundItem, name='datashow'),
    
]
