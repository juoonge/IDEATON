from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import News,Hreviews,Mreviews

# 뉴스 
def home(request):
    news=News.objects.all()
    return render(request,'home.html',{'news':news})

def news_detail(request,id):
    dnews=get_object_or_404(News,pk=id)
    return render(request,'news_detail.html',{'dnews':dnews})

def news_register(request):
    return render(request,'news_register.html')

def news_create(request):
    new_news=News()
    new_news.title=request.POST['title']
    new_news.writer=request.POST['writer']
    new_news.body=request.POST['body']
    new_news.date=timezone.now()
    new_news.image=request.FILES['image']
    new_news.save()
    return redirect('news_detail',new_news.id)

# 병원 리뷰
def hospital_review(request):
    hreview=Hreviews.objects.all()
    return render(request,'hospital_review.html',{'hreview':hreview})

def hreview_detail(request,id):
    hreview=get_object_or_404(Hreviews,pk=id)
    return render(request,'hreview_detail.html',{'hreview':hreview})

def hreview_register(request):
    return render(request,'hreview_register.html')

def hreview_create(request):
    new_hreview=Hreviews()
    new_hreview.hospital=request.POST['hospital']
    new_hreview.nickname=request.POST['nickname']
    new_hreview.body=request.POST['body']
    new_hreview.date=timezone.now()
    new_hreview.image=request.FILES['image']
    new_hreview.save()
    return redirect('hreview_detail',new_hreview.id)

# 약품 리뷰
def medicine_review(request):
    mreview=Mreviews.objects.all()
    return render(request,'medicine_review.html',{'mreview':mreview})

def mreview_detail(request,id):
    mreview=get_object_or_404(Mreviews,pk=id)
    return render(request,'mreview_detail.html',{'mreview':mreview})

def mreview_register(request):
    return render(request,'mreview_register.html')

def mreview_create(request):
    new_mreview=Mreviews()
    new_mreview.medicine=request.POST['medicine']
    new_mreview.nickname=request.POST['nickname']
    new_mreview.body=request.POST['body']
    new_mreview.date=timezone.now()
    new_mreview.image=request.FILES['image']
    new_mreview.save()
    return redirect('mreview_detail',new_mreview.id)

def chat(request):
    return render(request,'chat.html')

# def hreview(request):
#     return render(request,'hospital_review.html')

# def mreview(request):
#     return render(request,'medicine_review.html')