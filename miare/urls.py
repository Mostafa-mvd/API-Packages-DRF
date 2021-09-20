from django.urls import path

from miare.views import CapacityReportView

app_name = 'miare-api'

urlpatterns = [
    path('interview-test/', CapacityReportView.as_view())
]
