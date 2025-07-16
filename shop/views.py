from rest_framework import views
from rest_framework import response

from click_up import ClickUp

from backent import settings
from shop.serializers import OrderSerializer

click_up = ClickUp(
    service_id=settings.CLICK_SERVICE_ID,
    merchant_id = settings.CLICK_MERCHANT_ID
)


class OrderCreate(views.APIView):
    serializer_class = OrderSerializer

    def post(self, request):
        """
        Create a new order
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        result = {
            "order": serializer.data
        }

        if serializer.data['payment_method'] == 'click':
            payment_link = click_up.initializer.generate_pay_link(
                id=serializer.data['id'],
                amount=serializer.data['total_cost'],
                return_url="https://uzum.uz"
            )
            result["payment_link"] = payment_link
            
        return response.Response(result)

