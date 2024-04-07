from django.shortcuts import render, redirect
from reportapp.models import Article
from django.contrib.auth.decorators import login_required
from reportapp.models import Article
from datetime import datetime 



# def ReportFoundItem(request):
#     articles = Article.objects.all()  # Fetch all articles from the database
#     return render(request, 'datashow.html', {'articles': articles})
#     return render(request, 'datashow.html', {'found_data': 'Data for found item'})

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
                print('Item reported successfully:')
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





    
     