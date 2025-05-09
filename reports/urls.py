from django.urls import path
from .views import *

urlpatterns = [
    path('', SimpleReportView.as_view(), name='simple-report'),
    path('generate-report/', ReportTaskView.as_view(), name='generate-report'),
    path('generate-report/', GenerateReportView.as_view(), name='generate_report'),
    path('report-status/<str:report_id>/', ReportStatusView.as_view(), name='report-status'),

    
]
    # feedbackreportgenerator/reports/urls.py

