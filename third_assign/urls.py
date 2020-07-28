"""third_assign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import media_app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.main,name="main"),
    path('diary',myapp.views.diary,name="diary"),
    path('next/<int:diary_id>',myapp.views.next,name="next"),
    path('previous/<int:diary_id>',myapp.views.previous,name="previous"),
    path('detail/<int:diary_id>',myapp.views.detail,name="detail"),
    path('write/',myapp.views.write,name="write"),
    path('rewrite/<int:diary_id>',myapp.views.rewrite,name="rewrite"),
    path('remove/<int:diary_id>',myapp.views.remove,name="remove"),
    path('media_app/index/',media_app.views.index,name="index"),
    path('remove_image/<int:profile_id>',media_app.views.remove_image,name="remove_image"),
    path('community',myapp.views.community,name="community"),

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)