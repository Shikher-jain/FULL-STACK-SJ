from django.urls import path
from .views import ItemListView

urlpatterns = [
    path('api/items/', ItemListView.as_view(), name='item-list'),
]
