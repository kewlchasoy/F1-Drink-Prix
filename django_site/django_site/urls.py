"""
URL configuration for django_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('', include('my_app.urls')),
    path('', include('invitation.urls')),
    path('', include('register.urls')),
    path('', include("django.contrib.auth.urls")),
]

# urlpatterns = [
#     path('', include('my_app.urls')),
#     path('', include("django.contrib.auth.urls")),
#     path('group/', include("invitation.urls")),
#     path('register/', r.register, name="register"),
#     path('create_page/', i.create_page, name='create_page'),
#     path('page/<str:code>/', i.page, name='page'),
#     path('add_user/<str:code>/', i.add_user, name='add_user'),
# ]
