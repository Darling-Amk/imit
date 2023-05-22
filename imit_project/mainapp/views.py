from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Главная
def index(request):
    return render(request,'index.html')

#Институт
def about(request):
    return render(request,'about.html')

#Абитуриентам
def abit(request):
    return render(request,'abit.html')

def pr_club(request):
    return render(request,'pr_club.html')

def employers(request):
    return render(request,'employers.html')

def news(request,nid):
    data = {'id':nid}
    return render(request,'news.html', context=data)