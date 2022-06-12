from django.urls import path
from Productos import views
from Productos.views import sardo, reggiano, provolone, catalogo

urlpatterns = [
    
    path('catalogo/', catalogo, name='Catalogo'),
    path('sardo/', sardo, name='Sardo'),
    path('regg/', reggiano, name='Reggiano'),
    path('prov/', provolone, name='Provolone'),
]
