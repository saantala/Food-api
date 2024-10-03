from django.urls import path
from .views import HelloOrderView, OrderCreationListView, OrderDetailView




urlpatterns = [
    # path('', HelloOrderView.as_view(), name='hello_world'),
    path('', OrderCreationListView.as_view(), name='create_order'),
    path('<int:order_id>', OrderDetailView.as_view(), name='list_order'),
]
