from django.contrib import admin
from django.urls import path
from articals.views import(
    articals_index,
    request_blood_post
    )

app_name='articals'

urlpatterns = [
    path('post/', articals_index, name='articals_index'),
    path('request_blood/', request_blood_post, name='request_blood_post'),
]