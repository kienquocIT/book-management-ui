from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import requests
from rest_framework.views import APIView

from shared.mask_view import mask_view
from shared.middleware import AttachAuthTokenMiddleware
from ui import settings


# Create your views here.
class BookListView(View):
    @mask_view(
        auth_require=True,
    )
    def get(self, request):
        return render(request, "bookList.html")

class BookListApiView(View):
    @mask_view(
        auth_require=True,
    )
    def get(self, request):
        query_string = request.META.get('QUERY_STRING', '')
        url = f'v1/books'
        if query_string:
            url = f'{url}?{query_string}'

        print(url)

        res_books = AttachAuthTokenMiddleware.call_api("GET",url, request, params=request.GET)
        return JsonResponse(res_books.json(), safe=False)

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
        menu_list = request.data.get('menu_list', [])

        data = {
            'title': title,
            'publisher': publisher,
            'authors': authors,
            'published_date': published_date,
            'total_copies': total_copies,
            'available_copies': available_copies,
            'menu_list': menu_list,
        }

        print(data)

        r = requests.post(url=f'{settings.API_URL}v1/books/', json=data)

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
        response = r.json()
        endpoint_demo =response.get('demo_file')

        if endpoint_demo:
            response['demo_file'] = f'{settings.API_URL}{endpoint_demo}'
        try:
            return JsonResponse(response, status=r.status_code, safe=False)
        except ValueError:
            return JsonResponse({"error": r.text}, status=r.status_code)

    def put(self, request, pk):
        title = request.data.get('title')
        publisher = request.data.get('publisher')
        authors = request.data.get('authors', [])
        published_date = request.data.get('published_date')
        total_copies = request.data.get('total_copies')
        available_copies = request.data.get('available_copies')
        menus = request.data.get('menus', [])

        print(f'request: {request.data}')

        data = {
            'title': title,
            'publisher': publisher,
            'authors': authors,
            'published_date': published_date,
            'total_copies': total_copies,
            'available_copies': available_copies,
            'menu_list': menus,
        }

        print(f'update: {data}')

        r = requests.put(url=f'{settings.API_URL}v1/books/{pk}', json=data)

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

class BookUploadApiView(APIView):
    def put(self, request, pk):
        formData = request.FILES

        print(f'formData: {formData}')

        r = requests.put(url=f'{settings.API_URL}v1/books/{pk}/upload', files=formData)
        try:
            return JsonResponse(r.json(), status=r.status_code, safe=False)
        except ValueError:
            return JsonResponse({"error": r.text}, status=r.status_code)


