import sympy as sp
# from sympy.core import rules
# sp.init_session()
x, y, z, t = sp.symbols('x y z t')

class Fuzzy():
  def __init__(self, harga=0, fasilitas=0, jarak=0):
    self.harga = harga
    self.fasilitas = fasilitas
    self.jarak = jarak
    self.derajat_keanggotaan = 0

  def liniear_turun(self,a,b,x):
    if x <= a:
      self.derajat_keanggotaan = 1
    elif x >= a and x <= b:
      self.derajat_keanggotaan = (b - x) / (b - a)
    elif x >= b:
      self.derajat_keanggotaan = 0
    return self.derajat_keanggotaan

  def linear_naik(self,a,b,x):
    if x <= a:
      self.derajat_keanggotaan = 0
    elif x >= a and x <= b:
      self.derajat_keanggotaan = (x-a) / (b-a)
    elif x >= b:
      self.derajat_keanggotaan = 1
    return self.derajat_keanggotaan
  
  def kurva_segitiga(self,a,b,c,x):
    if x <= a or x >= c:
      self.derajat_keanggotaan = 0
    elif x >= a and x <= b:
      self.derajat_keanggotaan = (x-a) / (b-a)
    elif x >= b and x <= c:
      self.derajat_keanggotaan = (b-x) / (c-b)
    return self.derajat_keanggotaan


  # def get_result(self):
  #   my_dict = {
  #     'murah': self.murah(),
  #     'sedang': self.sedang(),
  #     'mahal': self.mahal()
  #   }
  #   return max(my_dict, key=my_dict.get)


class FuzzyWisata(Fuzzy):
  def __init__(self, harga, fasilitas, jarak):
    super().__init__(harga, fasilitas, jarak)

  def harga_murah(self):
    return super().liniear_turun(25000, 50000, self.harga)

  def harga_sedang(self):
    return super().kurva_segitiga(25000, 50000, 100000, self.harga)

  def harga_mahal(self):
    return super().linear_naik(50000, 100000, self.harga)

  def get_result_harga(self):
    my_dict = {
      'murah': self.harga_murah(),
      'sedang': self.harga_sedang(),
      'mahal': self.harga_mahal()
    }
    return max(my_dict, key=my_dict.get)


  def jarak_dekat(self):
    return super().liniear_turun(5, 7, self.jarak)

  def jarak_sedang(self):
    return super().kurva_segitiga(5, 10, 15, self.jarak)

  def jarak_jauh(self):
    return super().linear_naik(12, 15, self.jarak)

  def get_result_jarak(self):
    my_dict = {
      'dekat': self.jarak_dekat(),
      'sedang': self.jarak_sedang(),
      'jauh': self.jarak_jauh()
    }
    return max(my_dict, key=my_dict.get)


  def fasilitas_sedikit(self):
    return super().liniear_turun(50, 70, self.fasilitas)

  def fasilitas_sedang(self):
    return super().kurva_segitiga(50, 70, 90, self.fasilitas)

  def fasilitas_banyak(self):
    return super().linear_naik(70, 90, self.fasilitas)

  def get_result_fasilitas(self):
    my_dict = {
      'sedikit': self.fasilitas_sedikit(),
      'sedang': self.fasilitas_sedang(),
      'banyak': self.fasilitas_banyak()
    }
    return max(my_dict, key=my_dict.get)
  



# class Jarak(Fuzzy):
  # def __init__(self, nilai):
  #   super().__init__(nilai)

  # def jarak_dekat(self):
  #   return super().liniear_turun(5, 7, self.nilai)

  # def jarak_sedang(self):
  #   return super().kurva_segitiga(5, 10, 15, self.nilai)

  # def jarak_jauh(self):
  #   return super().linear_naik(12, 15, self.nilai)

  # def get_result(self):
  #   my_dict = {
  #     'dekat': self.jarak_dekat(),
  #     'sedang': self.jarak_sedang(),
  #     'jauh': self.jarak_jauh()
  #   }
  #   return max(my_dict, key=my_dict.get)


# class Fasilitas(Fuzzy):
  # def __init__(self, nilai):
  #   super().__init__(nilai)

  # def fasilitas_sedikit(self):
  #   return super().liniear_turun(50, 70, self.nilai)

  # def fasilitas_sedang(self):
  #   return super().kurva_segitiga(50, 70, 90, self.nilai)

  # def fasilitas_banyak(self):
  #   return super().linear_naik(70, 90, self.nilai)

  # def get_result(self):
  #   my_dict = {
  #     'sedikit': self.fasilitas_sedikit(),
  #     'sedang': self.fasilitas_sedang(),
  #     'banyak': self.fasilitas_banyak()
  #   }
  #   return max(my_dict, key=my_dict.get)


class Rekomendasi(Fuzzy):
  def __init__(self, nilai):
    # super().__init__(nilai)
    self.nilai = nilai

  def rekomendasi(self):
    return super().linear_naik(50, 100, self.nilai)

  def tidak_rekomendasi(self):
    return super().liniear_turun(50, 100, self.nilai)

  def get_result(self):
    my_dict = {
      'rekomendasi': self.rekomendasi(), 
      'tidak_rekomendasi': self.tidak_rekomendasi(),
    }
    return max(my_dict, key=my_dict.get)


test = FuzzyWisata(80000, 30, 15)
# print(test.harga_murah())
# print(test.harga_sedang())
# print(test.harga_mahal())
# print(test.get_result_harga(),'\n')

# print(test.fasilitas_sedikit())
# print(test.fasilitas_sedang())
# print(test.fasilitas_banyak())
# print(test.get_result_fasilitas(),'\n')

# print(test.jarak_dekat())
# print(test.jarak_sedang())
# print(test.jarak_jauh())
# print(test.get_result_jarak(),'\n')


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

# print(rules)

def fuzzy_proses(rules):
  a_predikat = []
  Z = []
  for index, value in enumerate(rules):
    # print(index, value[0])

    a_predikat_i = min(value[0])
    a_predikat.append(a_predikat_i)

    if value[1] == 'rekomendasi':
      # print(f"{index} | rekom")
      eqn = sp.Eq(a_predikat_i, (x - 50) / 50) # untuk rekomendasi
    else:
      # print(f"{index} | not rekom")
      eqn = sp.Eq(a_predikat_i, (100 - x) / 50) # untuk tidak_rekomendasi
      
    z_i = sp.solve(eqn)
    Z.append(z_i[0])

  # print(a_predikat)
  # print(Z)

  pembilang = 0
  for index, value in enumerate(rules):
    temp = (a_predikat[index] * Z[index])
    pembilang += temp
  penyebut = sum(a_predikat)
  print(pembilang / penyebut)

  # print(Rekomendasi(pembilang / penyebut).get_result())
  result = Rekomendasi(pembilang / penyebut)
  print(f"rekomendasi : {result.rekomendasi()}")
  print(f"tdk rekomendasi : {result.tidak_rekomendasi()}")
  return result.get_result()

# fuzzy_proses(rules)