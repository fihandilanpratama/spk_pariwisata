from django.shortcuts import render
from rekomendasi.models import Wisata
# Create your views here.
def index(request):
  all_wisatas = Wisata.objects.all()
  context = {
    'title': 'objek wisata',
    'subtitle': 'SPK Pariwisata',
    'all_wisatas': all_wisatas,
  }
  return render(request, 'objekwisata/index.html', context)