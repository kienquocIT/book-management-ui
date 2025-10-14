from django.urls import path
from .views import UserListView, UserCreateView, UserCreateApiView, UserUpdateView, UserUpdateApiview, \
    UserUploadAvatarView

app_name = 'user'

urlpatterns = [
    path('', UserListView.as_view(), name='UserListView'),
    path('create-api', UserCreateApiView.as_view(), name='UserCreateApiView'),
    path('create', UserCreateView.as_view(), name='UserCreateView'),
    path('<int:pk>', UserUpdateView.as_view(), name='UserUpdateView'),

    path('api/<int:pk>', UserUpdateApiview.as_view(), name='UserUpdateApiView'),

    path('<int:pk>/avatar', UserUploadAvatarView.as_view(), name='UserUploadAvatarView'),
]