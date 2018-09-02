from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from numpy.distutils.from_template import template_name_re

# Create your views here.

class index(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'list'
    paginate_by = 5

def detail(request, post_id):
    obj= get_object_or_404(Post, pk=post_id)
    return render(request, "blog/detail.html", {'post':obj})