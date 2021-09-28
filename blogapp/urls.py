from django.urls import path
from . import views
app_name = 'blogapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('services',views.services,name='services'),
    path('teams',views.teams,name='teams'),
    path('api',views.testView.as_view(),name='test')
]
