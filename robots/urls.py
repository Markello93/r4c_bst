from django.urls import path

from .views import RobotAPIView

urlpatterns = [path("add_robot/", RobotAPIView.as_view(), name="adding_robot")]
