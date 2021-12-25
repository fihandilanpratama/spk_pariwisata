from django.contrib import admin
from django.core.handlers import wsgi
from .models import Wisata, Rule
# Register your models here.
class RuleAdmin(admin.ModelAdmin):
    """ menampilkan spesific column """
    list_display = ['nama', 'harga', 'fasilitas', 'jarak', 'hasil']
    search_fields =  ['nama', 'harga', 'fasilitas', 'jarak', 'hasil']
    # prepopulated_fields = {'slug': ('first_name', 'last_name', 'title')}

class WisataAdmin(admin.ModelAdmin):
    """ menampilkan spesific column """
    list_display = ['nama', 'keterangan']
    # search_fields =  ['nama', 'harga', 'fasilitas', 'jarak', 'hasil']
    # prepopulated_fields = {'slug': ('first_name', 'last_name', 'title')}
    
admin.site.register(Wisata, WisataAdmin)
admin.site.register(Rule, RuleAdmin)