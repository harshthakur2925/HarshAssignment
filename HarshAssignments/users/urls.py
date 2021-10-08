from django.urls import path
from . import views

app_name = "main"


urlpatterns = [


    path("register", views.register_request, name="register"),

path('user_details/', views.user_details,  name='user_details'),
path("login", views.login_request, name="login"),
path("", views.home,),
#path("homepage", views.login_request, name="homepage"),
path('homepage', views.home_view,),
path('edit', views.update,),
path('delete', views.destroy,),
path('user_updated', views.edit_view,),
path('user_deleted', views.delete_view,),
path('login_done', views.login_view,),


]