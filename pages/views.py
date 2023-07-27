from typing import Optional
from django.shortcuts import get_object_or_404,render
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from blogs.models import Post
from django.contrib.auth.decorators import login_required


class HomePageView(generic.base.TemplateView):
    template_name = 'pages/home.html'
    
    
    
class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name='pages/profile.html'
    context_object_name ='pro'
    
    def get_object(self):
        return get_object_or_404(get_user_model(),username=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # اضافه کردن پست‌های کاربر لاگین شده به context
        logged_in_user = self.request.user
        user_posts = Post.objects.filter(author=logged_in_user,Status=True)
        context['posts'] = user_posts
        
        return context


# @login_required
# def profile_view(request):
#     logged_in_user = request.user
#     user_profile = get_object_or_404(get_user_model(), username=logged_in_user)
#     user_posts = Post.objects.filter(author=logged_in_user)

#     context = {
#         'pro': user_profile,
#         'posts': user_posts,
#     }
#     return render(request, 'pages/profile.html', context)
