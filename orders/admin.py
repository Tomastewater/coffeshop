from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInLineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInLineAdmin
    ]
