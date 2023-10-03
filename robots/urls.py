from django.urls import path

from .views import RobotAPIView, WeekReportAPIView

urlpatterns = [
    path('add_robot/', RobotAPIView.as_view(), name='adding_robot'),
    path('week_report/', WeekReportAPIView.as_view(), name='download_report'),
]