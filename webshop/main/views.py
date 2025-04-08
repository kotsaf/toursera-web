from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def tours(request):
    return render(request, 'tours.html')

def feedbacks(request):
    return render(request, 'feedbacks.html')

def contacts(request):
    return render(request, 'contacts.html')