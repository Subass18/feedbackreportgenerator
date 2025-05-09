from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from .tasks import generate_report, generate_pdf_report
from .models import Report

class SimpleReportView(APIView):
    def get(self, request):
        return Response({"message": "Report generator is working!"})

class ReportTaskView(APIView):
    def get(self, request):
        task = generate_report.delay()  # Run the task in background
        return Response({"task_id": task.id, "message": "Report generation started"})

class GenerateReportView(APIView):
    def post(self, request, *args, **kwargs):
        report_data = {
            "name": request.data.get("name", "Sample Report"),
            "description": request.data.get("description", "")
        }

        task = generate_pdf_report.delay(report_data)
        return Response({"task_id": task.id, "message": "Report generation started"}, status=status.HTTP_202_ACCEPTED)

class ReportStatusView(APIView):
    def get(self, request, task_id, *args, **kwargs):
        task_result = AsyncResult(task_id)

        if task_result.state == 'SUCCESS':
            report = Report.objects.get(id=task_result.result)
            return Response({
                "status": "Completed",
                "pdf_file_url": report.pdf_file.url
            }, status=status.HTTP_200_OK)

        return Response({
            "status": "In Progress",
            "task_state": task_result.state
        }, status=status.HTTP_202_ACCEPTED)
