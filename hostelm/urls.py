"""
URL configuration for hostelm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from playground import views as pg_views 
from playground import views


admin.site.site_header = "BOUHostel"
admin.site.site_title = "Hostel Admin Portal"
admin.site.index_title = "Welcome to BOUHostel Portal"


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', pg_views.register, name='register'),
    path('', include('playground.urls')),
    # path('', include('admin_adminlte.urls'))
    path('rooms/', include('rooms.urls')),
    path('students/', include('students.urls')),
    path('foods/', include('foods.urls')),
    path('profile/', views.profile_view, name='profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html',
        success_url='/profile/'
    ), name='password_change'),
    path('', include('playground.urls')),   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)