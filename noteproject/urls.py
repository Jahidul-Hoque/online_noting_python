from django.urls import path,include
from django.contrib import admin
from noteproject import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notelist/',include('noting.urls')),
    path('logintonotelist/', views.index, name='index'),
    path('',include('login.urls')),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)