"""jarvis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from accounts import views
from main import views
urlpatterns = [
    path('',views.home,name='home'),
    #path('',views.new_classrep,name='registration'),
    url(r'^registration/$',views.new_classrep,name='registration'),
    #path('',views.reg,name='regsuccessful'),
    path('admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login_user.html'),name='login'),
]
