from django.urls import include, path
from . import views                      # поставили .  т.к. надимся в той же директории

app_name = 'blog'

urlpatterns = [    
    path('', views.all_blogs, name='all_blogs'), 
    #path('3', views.detail, name='detail'), 
    path('<int:blog_id>/', views.detail, name='detail'),  
]