from django.shortcuts import render,get_object_or_404
from .models import Haber,Kategori


# Create your views here.
def basesayfasi(request):
     kategoriler = Kategori.objects.all()
     return render(request,'base.html',{'kategoriler': kategoriler})
def anasayfa(request):
    haberler = Haber.objects.all()
    kategoriler = Kategori.objects.all()
    return render(request, 'anasayfa.html', {
        'haberler': haberler,
        'kategoriler': kategoriler
    })
def kategoriye_gore_haberler(request, kategori_id):
    kategori = get_object_or_404(Kategori,pk=kategori_id)
    haberler = Haber.objects.filter(kategori=kategori)
    context = {'haberler': haberler, 'kategori': kategori}
    return render(request, 'kategori.html', context)
def arama_sonuc(request):
    query = request.GET.get('q','')
    if query:
        haberler = Haber.objects.filter(baslik__icontains=query)
    else:
        haberler = Haber.objects.all()
    return render(request,'arama_sonuc.html',{'haberler':haberler,'query':query})
def detay_sayfa(request,id):
    haber = get_object_or_404(Haber, pk=id)
    diger_haberler = Haber.objects.filter(kategori=haber.kategori).exclude(pk=haber.pk)[:5]
    return render(request, 'detay_sayfa.html',{
        'haber':haber,
        'diger_haberler':diger_haberler,
        })
