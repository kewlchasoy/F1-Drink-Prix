from django.urls import path

from .views import add_user, create_page, page


urlpatterns = [
  path('create_page/', create_page, name='create_page'),
  path('group/<str:code>/', page, name='page'),
  path('add_user/<str:code>/', add_user, name='add_user'),
]