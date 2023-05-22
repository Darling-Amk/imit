from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Главная
def index(request):
    news = [1, 2, 3, 4, 5]
    news = [
        {
        'id':id,
        'title': f'news#{id}',
        'text':f'text{id} texttexttexttexttexttexttexttexttexttexttexttexttexttexttexttexttext',
             } for id in range(1,6)
    ]
    data = {'title': 'Петрозаводский государственный университет','news':news}
    return render(request,'index.html', context=data)

#Институт
def about(request):
    data = {'title': 'О сайте'}
    return render(request,'about.html', context=data)

#Абитуриентам
def abit(request):
    data = {'title': 'Абитуриентам'}
    return render(request,'abit.html', context=data)

def pr_club(request):
    data = {'title': 'КТП'}
    return render(request,'pr_club.html', context=data)

def employers(request):
    data = {'title':'Партнеры'}
    return render(request,'employers.html', context=data)

def news(request,nid):
    news = [1,2,3,4,5]
    if nid not in news:
        return render(request, 'error.html', context={'title':f'Новость №{nid}','text':'Не существует такой новости'})

    data = {'id': nid,'title':f'Новость №{nid}'}
    return render(request,'news.html', context=data)
