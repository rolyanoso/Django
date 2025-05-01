from django.urls import path
from . import views

urlpatterns = [
    path('',views.anasayfa,name='anasayfa'),
    path('kategori/<int:kategori_id>/',views.kategoriye_gore_haberler,name='kategori'),
    path('arama/',views.arama_sonuc,name='arama_sonuc'),
    path('haber/<int:id>/',views.detay_sayfa,name='detay_sayfa'),
]