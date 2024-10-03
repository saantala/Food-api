from django.urls import path
from .views import RegisterView, UserCreationView



urlpatterns = [
    path('', RegisterView.as_view(), name='hello_world'),
    path('register/', UserCreationView.as_view(), name='register'),
    
    
]

