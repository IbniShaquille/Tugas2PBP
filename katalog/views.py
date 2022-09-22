from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = CatalogItem.objects.all()
    context = {
        'list_items': data_barang_wishlist,
        'nama': 'Ibni Shaquille Syauqi Ibrahim',
        'studentId': '2106706735'
    }
    return render(request, "katalog.html", context)
