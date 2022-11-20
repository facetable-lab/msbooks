from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('msbooks_engine.urls')),
    path('', include('msbooks_books.urls')),
    path('', include('msbooks_orders.urls'))
]
