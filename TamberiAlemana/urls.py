from django.contrib import admin
from django.urls import path, include
from Productos import views
from Productos.views import productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Productos/', include('Productos.urls'))
]
