from django.contrib import admin
from .models import Haber,Kategori
# Register your models here.

class HaberAdmini(admin.ModelAdmin):
    list_display = ('baslik','yazar','yayin_tarihi','kategori')
    search_fields = ['baslik'.lower(),'icerik'.lower()]
admin.site.register(Haber)
admin.site.register(Kategori)