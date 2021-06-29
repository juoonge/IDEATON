"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import myapp.views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='home'),
    path('<str:id>',myapp.views.news_detail,name='news_detail'),
    path('register/',myapp.views.news_register,name='news_register'),
    path('create/',myapp.views.news_create,name='news_create'),
    
    path('hospital/', myapp.views.hospital_review, name='hospital_review'),
    path('hospital/<str:id>',myapp.views.hreview_detail,name='hreview_detail'),
    path('hospital/hreview_register/',myapp.views.hreview_register,name='hreview_register'),
    path('hospital/hreview_create/',myapp.views.hreview_create,name='hreview_create'),
    
    path('medicine/', myapp.views.medicine_review, name='medicine_review'),
    path('medicine/<str:id>',myapp.views.mreview_detail,name='mreview_detail'),
    path('medicine/mreview_register/',myapp.views.mreview_register,name='mreview_register'),
    path('medicine/mreview_create/',myapp.views.mreview_create,name='mreview_create'),
    
    path('chat/',myapp.views.chat, name='chat'),
    #path('hospitalreview/',myapp.views.hreview, name='hreview'),
    #path('medicinereview/',myapp.views.mreview, name='mreview'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
