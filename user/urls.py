from django.urls import path
from .views import UserListView, UserCreateView, UserCreateApiView

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('create-api', UserCreateApiView.as_view(), name='create-api'),
    path('create', UserCreateView.as_view(), name='create'),
]