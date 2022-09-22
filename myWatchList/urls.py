# TODO: Implement Routings Here

from django.urls import path
from myWatchList.views import show_json, show_json_by_id, show_xml, show_xml_by_id
from myWatchList.views import show_wishlist

app_name = 'myWatchList'

urlpatterns = [
    path('html/', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]
