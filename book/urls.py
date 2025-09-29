from django.urls import path
from .views import BookListView, BookCreateView, BookCreateApiView, BookUpdateView, BookUpdateApiView

app_name = "book"

urlpatterns = [
    path('', BookListView.as_view(), name='BookListView'),
    path('create/', BookCreateView.as_view(), name='BookCreateView'),
    path('create-api/', BookCreateApiView.as_view(), name='BookCreateApiView'),
    path('<uuid:pk>', BookUpdateView.as_view(), name='BookUpdateView'),
    path('api/<uuid:pk>', BookUpdateApiView.as_view(), name='BookUpdateApiView'),
]