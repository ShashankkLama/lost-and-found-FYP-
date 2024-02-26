from django.urls import path
from reportapp import views



urlpatterns = [
    path('report', views.ReportItemPage, name='report'),
    path('reportfound', views.ReportFoundItem, name='reportfound'),

    
    
]