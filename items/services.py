from django.conf import settings
from django.urls import reverse_lazy

import stripe

stripe.api_key = settings.STRIPE_API_KEY


def get_stripe_payment_intent(item):
    return stripe.PaymentIntent.create(
        amount=item.price,
        currency=item.currency
    )


def get_stripe_payment_session(request, items):

    return stripe.checkout.Session.create(
        mode='payment',
        success_url=_get_full_uri(request, 'items', 'payment-success'),
        cancel_url=_get_full_uri(request, 'items', 'payment-cancel'),
        line_items=get_all_items(items)
    )


def get_all_items(items):
    list_items = []
    for item in items:
        list_items.append({
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name
                },
                'unit_amount_decimal': item.price,
            },
            'quantity': 1
        })
    return list_items


def _get_full_uri(request, app: str, url_namespace: str):
    return request.build_absolute_uri(reverse_lazy(f'{app}:{url_namespace}'))
