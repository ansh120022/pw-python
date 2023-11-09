FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy

WORKDIR /code/test_task_with_playwright

COPY .. /code/test_task_with_playwright

RUN pip install -r requirements.txt
RUN playwright install chrome
