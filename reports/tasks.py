from celery import shared_task
import time
from django.core.files.base import ContentFile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.files.base import ContentFile


@shared_task
def generate_report():
    time.sleep(5)  # Simulate a long task (5 seconds)
    return "Report generated successfully!"


@shared_task
def generate_pdf_report(report_data):
    """Generates a PDF report asynchronously"""
    # Create a PDF in memory
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # You can modify this to match your actual report structure
    c.drawString(100, 750, f"Report for {report_data['name']}")
    c.drawString(100, 730, f"Description: {report_data['description']}")
    
    # Save the PDF into memory and return as a content file
    c.save()
    buffer.seek(0)
    
    # You could save this file to your models or return the content
    pdf_content = buffer.read()
    return ContentFile(pdf_content, name="report.pdf")

