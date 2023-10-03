import io
import json
from datetime import date

from django.http import FileResponse, HttpResponseNotFound, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from robots.forms import RobotCreateForm
from robots.service import from_db_to_excel


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


@method_decorator(csrf_exempt, name='dispatch')
class WeekReportAPIView(View):
    """Представление для загрузки недельного отчета о производстве роботов"""

    def get(self, request):
        wb, model_data = from_db_to_excel()

        if not model_data:
            return HttpResponseNotFound(
                {'За последнюю неделю не было произведено ни одного робота.'}
            )

        buffer = io.BytesIO()
        wb.save(buffer)
        buffer.seek(0)
        current_date = date.today().strftime('%Y-%m-%d')
        response = FileResponse(
            buffer,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response[
            'Content-Disposition'
        ] = f'attachment; filename=robot_data_for_{current_date}.xlsx'
        return response
