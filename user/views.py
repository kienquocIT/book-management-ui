from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from rest_framework.views import APIView

from ui import settings


class UserListView(View):
    def get(self, request):
        r = requests.get(url=f'{settings.API_URL}v3/users', params=request.GET)
        print(r.json())
        return render(request, "userList.html", {'users': r.json()})


class UserCreateView(View):
    def get(self, request):
        return render(request, "userCreate.html")
    def post(self, request):
        print("post")

class UserCreateApiView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        data = {
            'username': username,
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
        }

        r = requests.post(url=f'{settings.API_URL}v3/users/', data=data)
        return JsonResponse(r.json())

class UserUpdateView(View):
    def get(self, request, pk):
        return render(request, "userDetail.html", )

class UserUpdateApiview(APIView):
    def get(self, request, pk):
        r = requests.get(url=f'{settings.API_URL}v3/users/{pk}')
        return JsonResponse(r.json())

    def put(self, request, pk):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        data = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }

        r = requests.put(url=f'{settings.API_URL}v3/users/{pk}', data=data)
        return JsonResponse(r.json())

    def delete(self, request, pk):
        r = requests.delete(url=f'{settings.API_URL}v3/users/{pk}')
        if r.status_code == 204:
            return JsonResponse({
                'status': 'success',
            })
        else:
            return JsonResponse({})
