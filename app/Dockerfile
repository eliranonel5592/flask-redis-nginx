FROM python:3.11-slim

WORKDIR /app

# שכבת תלויות
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# קוד האפליקציה
COPY app/ /app/

# ברירת מחדל: נריץ gunicorn (יציב לפרודקשן)
EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "wsgi:app"]
