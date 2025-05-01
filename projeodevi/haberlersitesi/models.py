from django.db import models
from django.utils import timezone

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
    
class Haber(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    yayin_tarihi = models.DateTimeField(auto_now_add=True)
    yazar = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='haber_fotolari/',null=True,blank=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.baslik
    




