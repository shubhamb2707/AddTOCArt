from django.conf.urls import url , include
from . import views
app_name = 'shop'
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
	url(r'^admin/',(admin.site.urls)),
	url(r'^$', views.product_list, name='product_list'),
	url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

