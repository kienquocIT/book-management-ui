from django.urls import path
from .views import BookListView, BookCreateView, BookCreateApiView, BookUpdateView, BookUpdateApiView, \
    BookUploadApiView, BookListApiView

app_name = "book"

urlpatterns = [
    path('', BookListView.as_view(), name='BookListView'),
    path('api/', BookListApiView.as_view(), name='BookListApiView'),
    path('create/', BookCreateView.as_view(), name='BookCreateView'),
    path('create-api/', BookCreateApiView.as_view(), name='BookCreateApiView'),
    path('<uuid:pk>', BookUpdateView.as_view(), name='BookUpdateView'),
    path('api/<uuid:pk>', BookUpdateApiView.as_view(), name='BookUpdateApiView'),
    path('<uuid:pk>/upload', BookUploadApiView.as_view(), name='BookUploadApiView'),
]