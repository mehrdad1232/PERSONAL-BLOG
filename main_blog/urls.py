"""
URL configuration for main_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from . import views
from . import settings
from django.conf.urls.static import static
from blogs import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('category/',include('blogs.urls')),
    path('blog/<slug:slug>/',BlogsView.blog ,name="blogs"),
    path('blogs/search/', BlogsView.search, name="search"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)