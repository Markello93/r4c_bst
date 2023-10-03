import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from orders.forms import OrderCreateForm


@method_decorator(csrf_exempt, name='dispatch')
class OrderCreate(View):
    """View for creating order from json request."""

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = OrderCreateForm(data)
            if not form.is_valid():
                return JsonResponse({'errors': form.errors}, status=400)
            form.save_order()
            return JsonResponse({'message': 'Заказ успешно создан.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
