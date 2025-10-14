import time

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

from authentication.views import BaseProtectedView, BaseProtectedApiView
from shared.mask_view import mask_view
from ui import settings
from shared.middleware import AttachAuthTokenMiddleware

class UserListView(View):
    @mask_view(
        auth_require=True,
        template='user/userList.html',
        response_key = 'users',
        admin_require=True,
    )
    def get(self, request):
        r = AttachAuthTokenMiddleware.call_api("GET", "v3/users", request, params=request.GET)
        data = r.json() if r.status_code and r.status_code == 200 else {}
        return data, r.status_code
class UserCreateView(View):
    @mask_view(
        auth_require=True,
        admin_require=True,
        template='user/userCreate.html',
    )
    def get(self, request):
        return {}

class UserCreateApiView(APIView):
    @mask_view(
        admin_require=True,
        auth_require=True,
    )
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_staff = request.POST.get('is_staff')

        data = {
            'username': username,
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'is_staff': is_staff,
        }

        r = AttachAuthTokenMiddleware.call_api("POST", "v3/users/", request, data=data)

        return JsonResponse(r.json(), status=r.status_code)


class UserUpdateView(View):
    @mask_view(
        auth_require=True,
        admin_require=True,
        template='user/userDetail.html',
    )
    def get(self, request, pk):
        return {}

class UserUpdateApiview(APIView):
    @mask_view(
        auth_require=True,
    )
    def get(self, request, pk):
        r = AttachAuthTokenMiddleware.call_api("GET", f'v3/users/{pk}', request)
        print(r.status_code)
        if r.status_code and r.status_code == 200:
            response = r.json()
            endpoint_avt = response.get('avatar')

            if endpoint_avt:
                response['avatar'] = f'{settings.API_URL}{endpoint_avt}'
            print(response)
            return JsonResponse(response)
        else:
            return JsonResponse({"error": r.text}, status=r.status_code)

    def put(self, request, pk):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        data = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }

        r = AttachAuthTokenMiddleware.call_api("PUT", f'v3/users/{pk}', request, data=data)

        if r.status_code and r.status_code == 200:
            return JsonResponse(r.json(), status=r.status_code)
        else:
            return JsonResponse({"error": r.text}, status=r.status_code)

    def delete(self, request, pk):
        r = AttachAuthTokenMiddleware.call_api("DELETE", f'v3/users/{pk}', request)

        if r.status_code and r.status_code == 204:
            return JsonResponse({'state': 'Delete success'}, status=r.status_code)
        else:
            return JsonResponse({"error": r.text}, status=r.status_code)

class UserUploadAvatarView(APIView):
    @mask_view(
        admin_require=True,
        auth_require=True,
    )
    def put(self, request, pk):
        formData = request.FILES

        print(f'formData: {formData}')

        r = AttachAuthTokenMiddleware.call_api("PUT", f'v3/users/{pk}/avatar', request, files=formData)

        if r.status_code and r.status_code == 200:
            data = r.json()
            data['version'] = int(time.time())
            return JsonResponse(data, status=r.status_code)
        else:
            return JsonResponse({"error": r.text}, status=r.status_code)