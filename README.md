# Feedback Report Generator

A modular, scalable solution built with Django, Celery, PostgreSQL, and Docker Compose to asynchronously generate HTML and PDF reports based on student event data.

## Project Overview

The **Feedback Report Generator** processes student event data (like saved code or submitted code actions) to generate HTML and PDF reports asynchronously. The project integrates various technologies such as Django REST Framework (DRF), Celery, Redis, PostgreSQL, and Docker Compose to handle task management, storage, and efficient report generation.

## Features

- **Asynchronous Task Handling**: Uses Celery for background processing of report generation tasks.
- **HTML Report Generation**: Generates a report showing the student's actions and event order.
- **PDF Report Generation**: Generates a PDF based on the same event order as the HTML report.
- **Task Monitoring**: Monitor task status via Flower.
- **Database**: PostgreSQL is used to store event data, HTML reports, and PDFs.
- **Containerization**: The app is containerized using Docker Compose for easy deployment.
  
## Tech Stack

- **Backend Framework**: Django & Django REST Framework (DRF)
- **Database**: PostgreSQL 16
- **Asynchronous Processing**: Celery
- **Message Broker**: Redis
- **Task Monitoring**: Flower
- **PDF Generation**: ReportLab (or alternative HTML-to-PDF solution)
- **Containerization**: Docker Compose
- **Package Management**: Poetry

## Setup

Follow these steps to set up and run the project locally.

### Prerequisites

1. **Docker** and **Docker Compose** installed
2. **Poetry** for package management

### 1. Clone the Repository

```bash
git clone https://github.com/Subass18/feedbackreportgenerator.git
cd feedbackreportgenerator
