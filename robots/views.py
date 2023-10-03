import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from robots.forms import RobotCreateForm


@method_decorator(csrf_exempt, name="dispatch")
class RobotAPIView(View):
    """Представление для создания робота из json запроса."""

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8"))
            form = RobotCreateForm(data)
            if not form.is_valid():
                return JsonResponse({"errors": form.errors}, status=400)
            form.save_robot()
            return JsonResponse({"message": "Робот создан успешно."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
