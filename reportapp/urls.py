from django.urls import path
from reportapp import views



urlpatterns = [
    path('report', views.ReportItemPage, name='report'),
    # path('abc', views.ReportItemPOSTPage, name='abc')
]