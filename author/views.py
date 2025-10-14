from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import requests
from rest_framework.views import APIView

from shared.mask_view import mask_view
from ui import settings


# Create your views here.
class AuthorListView(View):
    @mask_view(
        auth_require=True,
    )
    def get(self, request):
        r = requests.get(f'{settings.API_URL}v1/books/authors', params=request.GET)
        print(r.json())
        return render(request, 'authorList.html', {'authors': r.json()})

class AuthorListAPIView(APIView):
    @mask_view(
        auth_require=True,
    )
    def get(self, request):
        r = requests.get(f'{settings.API_URL}v1/books/authors', params=request.GET)
        return JsonResponse(r.json(), status=r.status_code, safe=False)

class AuthorCreateView(View):
    def get(self, request):
        r = requests.get(f'{settings.API_URL}v1/books', params=request.GET)
        return render(request, 'authorCreate.html', {'books': r.json()})

class AuthorCreateApiView(APIView):
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        books = request.data.get('books', [])
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'books': books
        }

        print(data)

        r = requests.post(url=f'{settings.API_URL}v1/books/authors', data=data)

        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            print(r.text)
            return JsonResponse({})

class AuthorUpdateView(View):
    def get(self, request, pk):
        r = requests.get(f'{settings.API_URL}v1/books', params=request.GET)
        return render(request, "authorDetail.html", {'books': r.json()})

class AuthorUpdateApiView(APIView):
    def get(self, request, pk):
        r = requests.get(f'{settings.API_URL}v1/books/authors/{pk}', params=request.GET)
        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            print(r.text)
            return JsonResponse({})

    def put(self, request, pk):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        books = request.data.get('books', [])

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'books': books
        }

        r = requests.put(url=f'{settings.API_URL}v1/books/authors/{pk}', json=data)
        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            print(r.text)
            return JsonResponse({"error": r.text}, status=r.status_code)

    def delete(self, request, pk):
        r = requests.delete(url=f'{settings.API_URL}v1/books/authors/{pk}')
        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            return JsonResponse({"error": r.text}, status=r.status_code)