from django.contrib.auth import authenticate, login
from django.views import View
from news.models import News
from news.models import Topic
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect

from news.forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def index(request):
    context = {'news_list': News.objects.all()}
    return render(request, 'index.html', context)

def creation(request):
    if(not request.POST):
        return render(request, "creation.html")
    topic = Topic(name = request.POST['topic'])

    news = News(title = request.POST['header'], text = request.POST['main_text'], topic = topic)
    topic.save()
    news.save()
    return HttpResponseRedirect('/')

def personal(request):
    context = {'news_list': News.objects.all()}
    if(not request.GET):
        return render(request, 'personal.html', context)
    a = request.GET.getlist('personalTopic[]')
    b = News.objects.all()
    c = []
    for x in b:
        if str(x) in a:
            c.append(x)
    context = {'news_list': c}
    return render(request, 'personal.html', context)
