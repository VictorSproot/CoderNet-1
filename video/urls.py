from django.urls import path
from .views import *


urlpatterns = [
    path('<slug>/addcomment', addcomment, name='addcomment_course'),
    path('', category_list, name='category_video_list_url'),
    path('<slug>/', category_detail, name='category_video_detail_url'),
    path('<cat_name>/<slug>/', course_detail, name='course_detail_url')
]
