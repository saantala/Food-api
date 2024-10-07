from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'size', 'quantity', 'order_status', 'created_at', 'updated_at')  # Remove 'customer'
    list_filter = ('order_status', 'size') 
    search_fields = ('food_name',)  

admin.site.register(Order, OrderAdmin)
