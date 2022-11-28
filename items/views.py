from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Item
from .services import get_stripe_payment_session


def index_view(request):
    newest_items = Item.objects.order_by("-id")[:10]
    return render(request, "index.html", context={"newest_items": newest_items})


def buy_item_view(request, item_id):
    item = [get_object_or_404(Item, pk=item_id)]
    session = get_stripe_payment_session(request, item)
    return JsonResponse({'id': session.id})


def get_item_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    template = 'items/item.html'
    context = {
        'item': item
    }
    return render(request, template, context)


def success_view(request):
    return render(request, 'static/success.html')


def cancel_view(request):
    return render(request, 'static/cancel.html')
