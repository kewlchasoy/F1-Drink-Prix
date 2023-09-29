from django.urls import path

from .views import group_page


urlpatterns = [
    path('<str:code>/', group_page, name='group_page'),
]