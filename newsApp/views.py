from django.shortcuts import render
from .models import *
import datetime
def news(request):
    ads = Adds.objects.all()
    news = News.objects.all().order_by('-date')[:12]
    marquee = News.objects.all().order_by('-date')[:10]
    international_news = News.objects.filter(category__icontains='আন্তর্জাতিক').order_by('-date')[:3]
    national_news = News.objects.filter(category__icontains='জাতীয়').order_by('-date')[:3]
    entertainment_news = News.objects.filter(category__icontains='বিনোদন').order_by('-date')[:3]
    play_news = News.objects.filter(category__icontains='খেলা').order_by('-date')[:3]
    context={
        'ads': ads,
        'news': news,
        'marquee': marquee,
        'international_news': international_news,
        'national_news': national_news,
        'entertainment_news': entertainment_news,
        'play_news': play_news,
    }
    return render(request, 'home.html', context)

def national(request):
    national_news = News.objects.filter(category__icontains='জাতীয়').order_by('-date')
    return render(request, 'national_news.html', {'national_news':national_news})
def international(request):
    international_news = News.objects.filter(category__icontains='আন্তর্জাতিক').order_by('-date')
    return render(request,'international_news.html',{'international_news': international_news})
def entertainment(request):
    entertainment_news = News.objects.filter(category__icontains='বিনোদন').order_by('-date')
    return render(request, 'entertainment_news.html', {'entertainment_news': entertainment_news})
def play(request):
    play_news = News.objects.filter(category__icontains='খেলা').order_by('-date')
    return render(request, 'play_news.html', {'play_news': play_news})
def news_details(request, pk):
    details = News.objects.get(pk=pk)
    return render(request, 'news_details.html',{'details': details})
def contract(request):
    return render(request, 'contract.html')
def search(request):
    news = News.objects.all()
    if request.method == "GET":
        nt = request.GET.get('que')
        if nt != None:
            news = News.objects.filter(title__icontains=nt)
    context={
        'news': news
    }
    return render(request, 'base.html', context)





