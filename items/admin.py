from django.contrib import admin

from .models import Item, Order, OrderItem

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description',
        'price',
    ]
    empty_value_display = 'Еще не указано'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    empty_value_display = 'Еще не указано'


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ['id', 'order', 'item']
    empty_value_display = 'Еще не указано'
