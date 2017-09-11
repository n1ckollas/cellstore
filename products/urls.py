from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
# from ecm.views import *
from products.views import *


urlpatterns = [
	url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name = 'product_detail'),
	url(r'^$', ProductListView.as_view(), name = 'products'),
	url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name = 'product_inventory')


]
