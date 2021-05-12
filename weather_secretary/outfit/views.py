from django.shortcuts import render
# Create your views here.

def outfit(request):
    return render(request, 'outfit.html')