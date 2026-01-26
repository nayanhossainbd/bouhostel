


from django.contrib.auth import views
from rooms import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('rooms_list/', views.rooms_list, name='rooms_list')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)