from django.shortcuts import render

def index(request):
    return render(request, 'webs/index.html')

def about(request):
    return render(request, 'webs/about.html')

def contact(request):
    return render(request, 'webs/contact.html')
