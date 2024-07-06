from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [


    path("",Home,name='Home'),
    path('login-page/',Login,name='Login'),
    path('sign-in/',Sign_in,name='Sign-in'),
    path('logout/',Logout,name='Logout'),
    path('Blog/<str:blog_id>/',Blog_page,name='Blog'),
    path('add-blog/',Add_blog,name='Add-blog'),
    path('update-blog/<str:blog_id>/',Update_blog,name='Update-blog'),
    path('delete-blog/<str:blog_id>/',Delete_blog,name='Delete-blog'),
    path('delete-comment/<str:comment_id>/',Delete_comment,name='Delete-comment'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)