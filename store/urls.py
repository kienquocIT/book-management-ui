from django.urls import path

from store.views import StoreListView, StoreListApiView, StoreCreateView, StoreCreateApiView, StoreDetailView, \
    StoreDetailApiView, StoreMoveBookView, StoreMoveBookApiView, SaleBookApiView

app_name = 'store'

urlpatterns = [
    path('', StoreListView.as_view(), name='storeListView'),
    path('api', StoreListApiView.as_view(), name='storeListApiView'),
    path('create', StoreCreateView.as_view(), name='storeCreateView'),
    path('create-api/', StoreCreateApiView.as_view(), name='storeCreateApiView'),
    path('<uuid:id>', StoreDetailView.as_view(), name='storeDetailView'),
    path('api/<uuid:id>', StoreDetailApiView.as_view(), name='storeDetailApiView'),
    path('move', StoreMoveBookView.as_view(), name='storeMoveBookView'),
    path('move-api', StoreMoveBookApiView.as_view(), name='storeMoveBookApiView'),
    path('sale', SaleBookApiView.as_view(), name='saleBookApiView'),
]