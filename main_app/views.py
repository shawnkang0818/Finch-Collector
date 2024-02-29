from django.shortcuts import render

from django.http import HttpResponse

# Create views
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')