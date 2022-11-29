from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('buy/<int:item_id>/', views.buy_item_view, name='buy_item'),
    path('item/<int:item_id>/', views.get_item_view, name='get_item'),
    path('order/<int:order_id>/', views.get_order_view, name='get_order'),
    path(
        'buy_order/<int:order_id>/',
        views.buy_multiple_items_view,
        name='buy_order'
    ),
    path('cancel/', views.cancel_view, name='payment-cancel'),
    path('success/', views.success_view, name='payment-success')
]
