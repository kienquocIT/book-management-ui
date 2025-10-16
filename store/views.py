import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from ui import settings


class StoreListView(View):
    def get(self, request):
        return render(request, 'storeList.html', {})

class StoreListApiView(APIView):
    def get(self, request):
        r = requests.get(f'{settings.API_URL}v1/books/stores', params=request.GET)
        print(r.json())
        return JsonResponse(r.json(), status=r.status_code, safe=False)

class StoreCreateView(View):
    def get(self, request):
        return render(request, 'storeCreate.html', {})

class StoreCreateApiView(APIView):
    def post(self, request):
        name = request.data.get('name')
        location = request.data.get('location')
        book_in_store = request.data.get('book_in_store', [])

        data = {
            'name': name,
            'location': location,
            'book_in_store': book_in_store,
        }

        print(data)
        r = requests.post(url=f'{settings.API_URL}v1/books/stores', json=data)
        return JsonResponse(r.json(), status=r.status_code, safe=False)

class StoreDetailView(View):
    def get(self, request, id):
        return render(request, 'storeDetail.html', {})

class StoreDetailApiView(APIView):
    def get(self, request, id):
        r = requests.get(f'{settings.API_URL}v1/books/stores/{id}', params=request.GET)
        print(r.json())
        return JsonResponse(r.json(), status=r.status_code, safe=False)

    def put(self, request, id):
        name = request.data.get('name')
        location = request.data.get('location')
        book_in_store = request.data.get('book_in_store', [])

        data = {
            'name': name,
            'location': location,
            'book_in_store': book_in_store,
        }

        r = requests.put(url=f'{settings.API_URL}v1/books/stores/{id}', json=data)
        return JsonResponse(r.json(), status=r.status_code, safe=False)

    def delete(self, request, id):
        r = requests.delete(f'{settings.API_URL}v1/books/stores/{id}', params=request.GET)
        return JsonResponse({'message': 'delete succes'}, status=r.status_code, safe=False)

class StoreMoveBookView(View):
    def get(self, request):
        return render(request, "moveBooks.html", {})

class StoreMoveBookApiView(APIView):
    def post(self, request):
        from_store_id = request.data.get('from_store_id')
        to_store_id = request.data.get('to_store_id')
        book_id = request.data.get('book_id')
        copies = request.data.get('copies')

        data = {
            'from_store_id': from_store_id,
            'to_store_id': to_store_id,
            'book_id': book_id,
            'copies': copies,
        }
        r = requests.post(url=f'{settings.API_URL}v1/books/stores/trans', json=data)
        return JsonResponse(r.json(), status=r.status_code, safe=False)

class SaleBookApiView(APIView):
    def post(self, request):
        sales = request.data

        print(sales)

        r = requests.post(
            url=f"{settings.API_URL}v1/books/stores/sale",
            json=sales
        )


        return JsonResponse(r.json(), status=r.status_code, safe=False)