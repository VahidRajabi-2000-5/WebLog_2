from typing import Optional
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required


from .models import Post
from .forms import NewPostForm




class PostsListView(generic.ListView):
    template_name = 'blogs/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(Status=True).order_by('-datetime_modified')



class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/post_detail.html'
    context_object_name = 'post'
    



class PostCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = NewPostForm
    template_name = 'blogs/post_create.html'
    context_object_name = 'form'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blogs/post_create.html'
    context_object_name = 'form'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blogs/post_delete.html'
    context_object_name ='post'
    success_url = reverse_lazy('posts_list')
        
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


    
    