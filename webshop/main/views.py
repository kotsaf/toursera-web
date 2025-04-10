from django.shortcuts import render
from .models import Feedback

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def tours(request):
    return render(request, 'tours.html')

def feedbacks(request):
    feedbacks = Feedback.objects.all
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})

def contacts(request):
    return render(request, 'contacts.html')