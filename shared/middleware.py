import requests
from django.shortcuts import redirect
from ui import settings


class AttachAuthTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.COOKIES.get("access_token")
        request.auth_headers = {}

        if token:
            request.auth_headers = {"Authorization": f"Bearer {token}"}

        response = self.get_response(request)
        return response

    @staticmethod
    def call_api(method, url, request, **kwargs):
        headers = kwargs.pop("headers", {})
        auth_headers = getattr(request, "auth_headers", {})
        headers.update(auth_headers)

        r = requests.request(method, f"{settings.API_URL}{url}", headers=headers, **kwargs)

        return r