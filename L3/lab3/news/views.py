from django.shortcuts import render
from news.models import News
def index(request):
    context = {'news_list': News.objects.all()}
    return render(request, 'index.html', context)

def creation(request):
    if(not request.POST):
        return render(request, "creation.html")
    articleHeader = request.POST['header']
    news = News(title = request.POST['header'], text = request.POST['main_text'])
    news.save()
    context = {'news_list': News.objects.all()}
    return render(request, 'index.html', context)