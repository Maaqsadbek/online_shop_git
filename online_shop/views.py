from django.shortcuts import render
from online_shop.models import *
from django.db.models import Q


# Create your views here.
def index(request):
    menyu = Maxsulotlar.objects.all()
    chegirmalar = Chegirmalar.objects.all()
    mijozlar1 = Happy_clents1.objects.all()
    mijozlar2 = Happy_clents2.objects.all()
    mijozlar3 = Happy_clents3.objects.all()
    max_idlar = Maxsulotlar.objects.all()
    max_id = [1]
    for i in max_idlar:
        max_id.append(i.id)
    new_id = max(max_id)
    new_id = new_id + 1
    chek_idlar = Chegirmalar.objects.all()
    chek_id = [0]
    for i in chek_idlar:
        chek_id.append(i.id)
    new_chek_id = max(chek_id)
    new_id += new_chek_id
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
#### Search bilan iwlash#############
    #if "Search" in request.POST:
     #   if not (request.POST.get("Search") is None):
      #      malumot = request.POST.get("Search").strip()
       #     qidiruv = Q(nomi__startswith = malumot) | Q(turi__startswith = malumot) | Q(
        #        new_prise__startswith = malumot) | Q(rangi__startswith = malumot) | Q(desc__startswith = malumot) | Q(
         #       tur__nomi__startswith = malumot) | Q(rang__nomi__startswith = malumot)
            #try:
             #   Maks = Maxsulotlar.objects.filter(qidiruv)
            #except Exception as s:
             #   print(s)

    return render(request, 'index.html',
                  { "new_id": new_id, 'menyu': menyu, 'chegirmalar': chegirmalar, 'mijozlar1': mijozlar1,
                   'mijozlar2': mijozlar2, 'mijozlar3': mijozlar3})


def contact(request):
    if "ariza" in request.POST:
        if not (request.POST.get("ariza") is None):
            ism = request.POST.get("ism")
            fam = request.POST.get("fam")
            ish_joy = request.POST.get("ish")
            adres = request.POST.get("adres")
            tel_number = request.POST.get("tell")
            maxsulot_nomi = request.POST.get('message')

            Arizalar(Arizalar.soni + 1, ism, fam, ish_joy, adres, tel_number, maxsulot_nomi).save()
        ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
    return render(request, 'contact.html')


def product(request):
    menyu = Maxsulotlar.objects.all()
    chegirma_menyu = Chegirmalar.objects.all()
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()

    return render(request, 'product.html', {'menyu': menyu, 'chegirma_menyu': chegirma_menyu})


def services(request):
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
    return render(request, 'services.html')


def single(request):
    ##Bittalik email uchun##
    if "Email" in request.POST:
        if not (request.POST.get("Email") is None):
            gmail = request.POST.get("Email")
            idlar = [0]
            gmaillar = Onemail.objects.all()
            for page in gmaillar:
                idlar.append(page.id)
            new_id = max(idlar)
            Onemail(new_id + 1, gmail).save()
    return render(request, 'single.html')
