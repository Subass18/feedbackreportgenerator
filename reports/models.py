from django.db import models

# feedbackreportgenerator/reports/models.py
from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
