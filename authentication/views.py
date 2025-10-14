import jwt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from jwt import ExpiredSignatureError, InvalidTokenError

import requests

from shared.mask_view import mask_view
from ui import settings


class BaseProtectedView(View):
    def dispatch(self, request, *args, **kwargs):
        token = request.COOKIES.get("access_token")
        if not token:
            return redirect("authentication:AuthenticationLogin")

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_API_KEY,
                algorithms=["HS256"],
            )
        except ExpiredSignatureError:
            return redirect("authentication:AuthenticationLogin")
        except InvalidTokenError:
            return redirect("authentication:AuthenticationLogin")

        return super().dispatch(request, *args, **kwargs)


class BaseProtectedApiView(APIView):
    def dispatch(self, request, *args, **kwargs):
        token = request.COOKIES.get("access_token")
        if not token:
            return redirect("authentication:AuthenticationLogin")

        return super().dispatch(request, *args, **kwargs)


class AuthenticationLoginView(View):
    @mask_view(
        auth_require=False,
        template="login.html",
    )
    def get(self, request):
        return None

class AuthenticationLoginApiView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        data = {
            'username': username,
            'password': password
        }

        r = requests.post(url=f'{settings.API_URL}v3/users/login', json=data)
        response_data = r.json()

        token = response_data.get('access')

        response = JsonResponse(response_data, status=r.status_code)

        if token:
            response.set_cookie(
                key="access_token",
                value=token,
                httponly=True,
                secure=True,
                samesite="Lax"
            )
        return response


class AuthenticationLogoutApiView(APIView):
    def post(self, request):
        response = JsonResponse({
            "message": "Logged out successfully"
        })

        response.delete_cookie("access_token")

        return response


class AuthenticationRegisterView(View):
    @mask_view(
        auth_require=False,
        template="register.html",
    )
    def get(self, request):
        return None


class AuthenticationRegisterApiView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')

        data = {
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        r = requests.post(url=f'{settings.API_URL}v3/users/register', json=data)
        response_data = r.json()
        return JsonResponse(response_data)
