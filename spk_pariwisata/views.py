from django.shortcuts import render

def index(request):
  context = {
    'title': 'home',
    'subtitle': 'SPK Pariwisata',
  }
  return render(request, 'index.html', context)