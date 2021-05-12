from django.shortcuts import render

# Create your views here.
def weather_page(request):
    return render (request, 'weather_page.html')
    