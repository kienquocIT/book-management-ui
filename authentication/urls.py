from django.urls import path

from authentication.views import AuthenticationLoginView, AuthenticationLoginApiView, AuthenticationLogoutApiView, \
    AuthenticationRegisterView, AuthenticationRegisterApiView

app_name = 'authentication'

urlpatterns = [
    path('', AuthenticationLoginView.as_view(), name='AuthenticationLogin'),
    path('login/', AuthenticationLoginApiView.as_view(), name='AuthenticationApiLogin'),
    path('logout/', AuthenticationLogoutApiView.as_view(), name='AuthenticationLogoutApi'),
    path('register', AuthenticationRegisterView.as_view(), name='AuthenticationRegister'),
    path('register/api', AuthenticationRegisterApiView.as_view(), name='AuthenticationRegisterApi'),
]