from click_up.views import ClickWebhook

from click_up.models import ClickTransaction

from shop.models import Order

class ClickWebhookAPIView(ClickWebhook):
    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )
        order = Order.objects.get(id=transaction.account_id)
        order.is_paid = True
        order.save()

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )

