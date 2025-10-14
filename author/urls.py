from django.urls import path

from author.views import AuthorListView, AuthorCreateView, AuthorCreateApiView, AuthorUpdateView, AuthorUpdateApiView, \
    AuthorListAPIView

app_name = 'author'

urlpatterns = [
    path('', AuthorListView.as_view(), name='AuthorListView'),
    path('api', AuthorListAPIView.as_view(), name='AuthorListAPI'),
    path('create', AuthorCreateView.as_view(), name='AuthorCreateView'),
    path('create-api', AuthorCreateApiView.as_view(), name='AuthorCreateApiView'),
    path('<uuid:pk>', AuthorUpdateView.as_view(), name='AuthorUpdateView'),
    path('api/<uuid:pk>', AuthorUpdateApiView.as_view(), name='AuthorUpdateApiView'),
]