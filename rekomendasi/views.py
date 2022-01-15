from django.shortcuts import render
from .models import Wisata, Rule
from .fuzzy import FuzzyWisata, fuzzy_proses

# Create your views here.
def index(request):
  all_wisatas = Wisata.objects.all()
  context = {
    'title': 'rekomendasi',
    'subtitle': 'SPK Pariwisata',
    'all_wisatas': all_wisatas,
  }
  if request.method == 'POST':
    # jika tombol submit form criteria (harga, fasilitas, jarak) ditekan
    if 'criteria_submit' in request.POST:
      # tangkap variabel
      harga = float(request.POST['harga'])
      fasilitas = float(request.POST['fasilitas'])
      jarak = float(request.POST['jarak'])

      # proses kriteria
      test = FuzzyWisata(harga, fasilitas, jarak)

      print(f"harga : {test.get_result_harga()}")
      print(f"fasilitas : {test.get_result_fasilitas()}")
      print(f"jarak : {test.get_result_jarak()}")

      rules = [
        [[test.harga_murah(), test.fasilitas_sedikit(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_murah(), test.fasilitas_sedikit(), test.jarak_sedang()], 'rekomendasi'],
        [[test.harga_murah(), test.fasilitas_sedikit(), test.jarak_jauh()], 'rekomendasi'],
        [[test.harga_murah(), test.fasilitas_sedang(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_murah(), test.fasilitas_sedang(), test.jarak_sedang()], 'rekomendasi'],
        [[test.harga_murah(), test.fasilitas_sedang(), test.jarak_jauh()], 'tidak_rekomendasi'],
        [[test.harga_murah(), test.fasilitas_banyak(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_murah(), test.fasilitas_banyak(), test.jarak_sedang()], 'rekomendasi'],
        [[test.harga_murah(), test.fasilitas_banyak(), test.jarak_jauh()], 'rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_sedikit(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_sedikit(), test.jarak_sedang()], 'rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_sedikit(), test.jarak_jauh()], 'tidak_rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_sedang(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_sedang(), test.jarak_sedang()], 'rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_sedang(), test.jarak_jauh()], 'tidak_rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_banyak(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_banyak(), test.jarak_sedang()], 'rekomendasi'],
        [[test.harga_sedang(), test.fasilitas_banyak(), test.jarak_jauh()], 'tidak_rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_sedikit(), test.jarak_dekat()], 'tidak_rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_sedikit(), test.jarak_sedang()], 'tidak_rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_sedikit(), test.jarak_jauh()], 'tidak_rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_sedang(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_sedang(), test.jarak_sedang()], 'tidak_rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_sedang(), test.jarak_jauh()], 'tidak_rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_banyak(), test.jarak_dekat()], 'rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_banyak(), test.jarak_sedang()], 'rekomendasi'],
        [[test.harga_mahal(), test.fasilitas_banyak(), test.jarak_jauh()], 'tidak_rekomendasi'],
      ]

      hasil_keputusan = fuzzy_proses(rules)
      print('\n',hasil_keputusan,'\n')
      context['hasil_keputusan'] = hasil_keputusan

      nama_wisata = request.POST['nama']
      context['selected_wisata'] = Wisata.objects.get(nama = nama_wisata)

      context['jarak'] = request.POST['jarak']

    # jika tidak ada wisata yang dipilih
    else:
      if request.POST['nama_wisata'] == 'none':
        pass
      else:
        nama_wisata = request.POST['nama_wisata']
        context['selected_wisata'] = Wisata.objects.get(nama = nama_wisata)

  return render(request, 'rekomendasi/index.html', context)