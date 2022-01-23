
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from UserProfile.views import(
    registrations,
    login,
    index,
    logout_view,
    user_profile,
    update_profile,
    search_donor,
    About_Blood,
    )

app_name='UserProfile'

urlpatterns = [
    path('', index, name='index'),
    path('registrations/', registrations, name='registrations'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('User/<str:username>', user_profile, name='user_profile'),
    path('update_profile/<str:username>', update_profile, name='update_profile'),
    path('search_donor/', search_donor, name='search_donor'),
    path('About_Blood/', About_Blood, name='About_Blood'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)