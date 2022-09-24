from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class DetailblogVIew(DetailView):
    model = Post
    template_name = 'detailpost.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title','author','body']
    template_name = 'createpost.html'
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'edit_post.html'
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'del_post.html'
    success_url = reverse_lazy('home')

