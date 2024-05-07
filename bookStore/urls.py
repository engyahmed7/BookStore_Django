from django.urls import path
from . import views

app_name = 'bookStore';

urlpatterns = [
    path('', views.index, name='getAll'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.show, name='show'),
    # path('store', views.store, name='store'),
    path('<int:pk>/delete', views.destroy, name='destroy'),
    path('<int:pk>/update', views.update, name="update"),
]
