from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'size','food_name', 'quantity', 'order_status', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'order_status', 'size']
    search_fields = ['customer__username', 'customer__email']