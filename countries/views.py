from django.shortcuts import render
from countries.models import Country


def get_countries(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        return render(request, 'countries/index.html', {'countries': countries})


def get_country(request, id):
    if request.method == 'GET':
        country = Country.objects.get(id=id)
        return render(request, 'countries/detail.html', {'country': country})


def post_country(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        capital = request.POST.get('capital')
        flag = request.FILES.get('flag')
        hymn = request.POST.get('hymn')
        population = request.POST.get('population')
        total_area = request.POST.get('total_area')
        post_obj = Country.objects.create(name=name, capital=capital, flag=flag, hymn=hymn, population=population, total_area=total_area)
    return render(request, 'countries/create.html')