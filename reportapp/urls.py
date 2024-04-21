from django.urls import path
from reportapp import views

urlpatterns = [
    path('report', views.ReportLostItem, name='report'),
    path('reportfound', views.ReportFoundItem, name='reportfound'),
    path('viewitems', views.viewItems, name='viewitems'),
   
]
