
from django.conf.urls import include, url 

from django.urls import include, path


from django.contrib import admin 


urlpatterns = [
	path('shop/', include('shop.urls',namespace='shop')),
	path('admin/',admin.site.urls),
	
]

