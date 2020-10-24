from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView,CreateView,DetailView
from .models import Post


def index(request):
    posts=Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

class PageCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title','cover','image')



class PageDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    fields=('title','cover','image')

