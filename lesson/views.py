from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from lesson.models import Article, Comments
from lesson.forms import CommentForm
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib import auth
# Create your views here.

def articles(request):
    return render(request, 'articles.html', {'articles':Article.objects.all(), 'username':auth.get_user(request).username})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article.html', args)


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(str(article_id), "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/article/get/%s/' %article_id)