from django.shortcuts import render, redirect
from reportapp.models import Article
from django.contrib.auth.decorators import login_required
from reportapp.models import Article
from datetime import datetime 
from asgiref.sync import async_to_sync
from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
import json
from django.http import HttpResponse


def ReportLostItem(request):
    if request.method == 'POST':
        user = request.user if request.user.is_authenticated else None

        if user:
            
            try:
                name = request.POST.get('name')
                brand = request.POST.get('brand')
                category = request.POST.get('category')
                lostlocation = request.POST.get('lostlocation')
                lostdate= request.POST.get('lostdate')
                description = request.POST.get('description')
                status = "Lost"
                
                if not all([name, brand, category, lostlocation, lostdate, description]):
                    error_message = "Please fill out all the empty fields."
                    return render(request, 'reportlost.html', {'error_message': error_message})
                
                try:
                # Convert the date string to a datetime object
                    lostdate = datetime.strptime(lostdate, '%Y-%m-%d').date()
                except ValueError:
                    lostdate = None

                article = Article.objects.create(
                    user=user,
                    name=name,
                    brand=brand,
                    category=category,
                    lostlocation=lostlocation,
                    lostdate=lostdate,
                    description=description,
                    status=status,
                )
                
                
                
                # Print additional information after successful creation
                print('User:', article.user.username)
                print('Name:', article.name)
                print('Brand:', article.brand)
                print('Category:', article.category)
                print('Lost Location:', article.lostlocation)
                print('Description:', article.description)

                print('The lost item has been reported successfully.')

                # Redirect to another template after successful creation
                # alert_message = "Item reported successfully!"
                # return render(request, 'datashow.html', {'alert_message': alert_message})
            except Exception as e:
                print('Error creating article:', e)

    return render(request, 'reportlost.html')


def ReportFoundItem(request):
    if request.method == 'POST':
        user = request.user if request.user.is_authenticated else None

        if user:
            
            try:
                name = request.POST.get('name')
                brand = request.POST.get('brand')
                category = request.POST.get('category')
                foundlocation = request.POST.get('foundlocation')
                founddate= request.POST.get('founddate')
                description = request.POST.get('description')
                status = "Found"
                
                if not all([name, brand, category, foundlocation, founddate, description]):
                    error_message = "Please fill out all the empty fields."
                    return render(request, 'reportlost.html', {'error_message': error_message})
                
                
                # Convert the date string to a datetime object
                founddate = datetime.strptime(founddate, '%Y-%m-%d').date()
                

                article = Article.objects.create(
                    user=user,
                    name=name,
                    brand=brand,
                    category=category,
                    foundlocation=foundlocation,
                    founddate=founddate,
                    description=description,
                    status=status,
                )
                
                
                
                # Print additional information after successful creation
                print('User:', article.user.username)
                print('Item reported successfully:')
                print('Name:', article.name)
                print('Brand:', article.brand)
                print('Category:', article.category)
                print('Found Location:', article.foundlocation)
                print('Description:', article.description)

                print('The found item has been reported successfully.')

                # Redirect to another template after successful creation
                # alert_message = "Item reported successfully!"
                # return render(request, 'datashow.html', {'alert_message': alert_message})
            except Exception as e:
                print('Error creating article:', e)

    return render(request, 'reportfound.html')


def viewItems(request):
    all_articles = Article.objects.all
    
    return render ( request, 'viewitems.html', {'all' : all_articles})


# def test(request):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "notification_broadcast",
#         {
#             'type': 'send_notification',
#             'message': json.dumps("Notification")
#         }
#     )
#     return HttpResponse("Done")


# def test(request):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "notification_broadcast",
#         {
#             'type': 'send_notification',
#             'message': json.dumps("Notification")
#         }
#     )
#     response = HttpResponse("Done")
#     response['Custom-Header'] = 'Value'  # Add your custom header here
#     return response
    
     