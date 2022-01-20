
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UserProfile.urls')),
    path('', include('articals.urls')),
]
