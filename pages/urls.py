from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('profile',views.ProfileView.as_view(),name='profile')
    # path('profile',views.profile_view,name='profile')
    
]
