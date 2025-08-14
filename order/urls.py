from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import  ClickWebhookView

urlpatterns = [
    path('payments/webhook/click/', csrf_exempt(ClickWebhookView.as_view()), name='click_webhook'),
]