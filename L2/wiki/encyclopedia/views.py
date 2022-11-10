from django.shortcuts import render
import markdown2
from . import util
import random

def index(request):
    if(not request.GET):
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })
    msg = request.GET['q']
    if(util.get_entry(msg)):
        return render(request, "encyclopedia/article.html", {
            "article": markdown2.markdown(util.get_entry(msg)),
            "name": util.get_entry(msg).split()[1] ,   
        })
    else:
        articles = []
        for article in util.list_entries():
            if(msg.lower() in article.lower()):
                articles.append(article)

        if(len(article)>0):
            return render(request, "encyclopedia/index.html", {
                "entries": articles
            })

def article(request, article):
    if(not request.GET):
        return render(request, "encyclopedia/article.html", {
            "article": markdown2.markdown(util.get_entry(request.path[5:])),
            "name": util.get_entry(request.path[5:]).split()[1] ,   
        })
    try:
        articleHeader = request.GET['header']
        util.save_entry(articleHeader, request.GET['main_text'])
        return render(request, "encyclopedia/article.html", {
            "article": markdown2.markdown(util.get_entry(articleHeader)),
            "name": util.get_entry(articleHeader).split()[1] ,   
        })

    except:
        return render(request, "encyclopedia/redact.html", {
            "article": util.get_entry(request.path[5:]),
            "name": util.get_entry(request.path[5:]).split()[1] ,   
        })


def randomArticle(request):
    articles = util.list_entries()
    article = random.choice(articles)
    return render(request, "encyclopedia/article.html", {
        "article": markdown2.markdown(util.get_entry(article)),
        "name": util.get_entry(article).split()[1] ,   
    })

def creation(request):
    if(not request.GET):
        return render(request, "encyclopedia/creation.html")
    articleHeader = request.GET['header']
    if(not originalityCheck(articleHeader)):
        return render(request, "encyclopedia/error.html")
    util.save_entry(articleHeader, request.GET['main_text'])

    return render(request, "encyclopedia/article.html", {
        "article": markdown2.markdown(util.get_entry(articleHeader)),
        "name": util.get_entry(articleHeader).split()[1] ,   
    })

def originalityCheck(name):
    for article in util.list_entries():
        if(name.lower() in article.lower()):
            return False
    return True

