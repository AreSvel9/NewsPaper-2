from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm
from .models import Post
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = '-dateCreation'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
