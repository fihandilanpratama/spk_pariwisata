from typing import Tuple
from django.db import models
# from django.db.models.fields import CharField

# Create your models here.
class Wisata(models.Model):
  nama = models.CharField(max_length=255)
  foto = models.ImageField(null=True, blank=True, upload_to='images/')
  keterangan = models.TextField()
  harga = models.IntegerField()
  jml_fasilitas = models.IntegerField()
  jarak = models.IntegerField()
  gm_url = models.TextField()

  # getter decorator untuk menampilkan foto wisata jika ada dan tampil foto default jika tidak ada
  @property
  def get_photo_url(self):
    if self.foto and hasattr(self.foto, 'url'):
        return self.foto.url
    else:
        return "/media/images/no-image.jpg"

  def __str__(self):
    return f"{self.nama} | {self.harga} | {self.jml_fasilitas}"


JARAK_OPTIONS = [
    # value, nama
    ('dekat', 'Dekat'),
    ('sedang', 'Sedang'),
    ('jauh', 'Jauh'),
]
HARGA_OPTIONS = [
    # value, nama
    ('murah', 'Murah'),
    ('sedang', 'Sedang'),
    ('mahal', 'Mahal'),
]
FASILITAS_OPTIONS = [
    # value, nama
    ('sedikit', 'Sedikit'),
    ('sedang', 'Sedang'),
    ('banyak', 'Banyak')
]
HASIL_OPTIONS = [
    # value, nama
    ('rekomendasi', 'Rekomendasi'),
    ('tidak_rekomendasi', 'Tidak Rekomendasi')
]

class Rule(models.Model):
    nama = models.CharField(max_length=10)
    harga = models.CharField(max_length=50, choices=HARGA_OPTIONS, default='nothing')
    fasilitas = models.CharField(max_length=50, choices=FASILITAS_OPTIONS, default='nothing')
    jarak = models.CharField(max_length=50, choices=JARAK_OPTIONS, default='nothing')
    hasil = models.CharField(max_length=50, choices=HASIL_OPTIONS, default='nothing')

    def __str__(self):
        return f"{self.id}"