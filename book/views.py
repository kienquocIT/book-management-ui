from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import requests
from rest_framework.views import APIView

from ui import settings


# Create your views here.
class BookListView(View):
    def get(self, request):
        res_books = requests.get(url=f'{settings.API_URL}v1/books', params=request.GET)
        res_authors = requests.get(url=f'{settings.API_URL}v1/books/authors', params=request.GET)
        return render(request, "bookList.html", {
            'books': res_books.json(),
            'authors': res_authors.json(),
        })

class BookCreateView(View):
    def get(self, request):
        res_authors = requests.get(url=f'{settings.API_URL}v1/books/authors', params=request.GET)
        return render(request, "bookCreate.html", {'authors': res_authors.json()})

class BookCreateApiView(APIView):
    def post(self, request):
        title = request.data.get('title')
        publisher = request.data.get('publisher')
        authors = request.data.get('authors', [])
        published_date = request.data.get('published_date')
        total_copies = request.data.get('total_copies')
        available_copies = request.data.get('available_copies')

        data = {
            'title': title,
            'publisher': publisher,
            'authors': authors,
            'published_date': published_date,
            'total_copies': total_copies,
            'available_copies': available_copies,
        }

        print(data)

        r = requests.post(url=f'{settings.API_URL}v1/books/', data=data)

        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            print(r.text)
            return JsonResponse({"error": r.text}, status=r.status_code)

class BookUpdateView(View):
    def get(self, request, pk):
        res_authors = requests.get(url=f'{settings.API_URL}v1/books/authors', params=request.GET)
        return render(request, "bookDetail.html", {'authors': res_authors.json()})

class BookUpdateApiView(APIView):
    def get(self, request, pk):
        r = requests.get(url=f'{settings.API_URL}v1/books/{pk}', params=request.GET)
        print(r.json())
        try:
            return JsonResponse(r.json())
        except ValueError:
            print(r.text)
            return JsonResponse({"error": r.text}, status=r.status_code)

    def put(self, request, pk):
        title = request.data.get('title')
        publisher = request.data.get('publisher')
        authors = request.data.get('authors', [])
        published_date = request.data.get('published_date')
        total_copies = request.data.get('total_copies')
        available_copies = request.data.get('available_copies')

        print(f'request: {request.data}')

        data = {
            'title': title,
            'publisher': publisher,
            'authors': authors,
            'published_date': published_date,
            'total_copies': total_copies,
            'available_copies': available_copies,
        }

        print(f'update: {data}')

        r = requests.put(url=f'{settings.API_URL}v1/books/{pk}', data=data)

        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            print(r.text)
            return JsonResponse({"error": r.text}, status=r.status_code)

    def delete(self, request, pk):
        r = requests.delete(url=f'{settings.API_URL}v1/books/{pk}')
        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            return JsonResponse({"error": r.text}, status=r.status_code)


