from django.shortcuts import render
from myWatchList.models import myWatchListItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = myWatchListItem.objects.all()
    context = {
        'films': data_barang_wishlist,
        'nama': 'Ibni Shaquille Syauqi Ibrahim',
        'studentId': '2106706735'
    }
    return render(request, "myWatchList.html", context)

def show_xml(request):
    data = myWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = myWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = myWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = myWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
