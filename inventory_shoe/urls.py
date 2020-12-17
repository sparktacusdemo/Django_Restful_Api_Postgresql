from django.conf.urls import url
from inventory_shoe import views

urlpatterns = [
    url(r'^api/inventory_shoe/$', views.inventory_shoe_list),
    url(r'^api/inventory_shoe/(?P<pk>[0-9]+)$', views.inventory_shoe_detail),
    url(r'^api/inventory_shoe/available$', views.inventory_shoe_list_available),
]