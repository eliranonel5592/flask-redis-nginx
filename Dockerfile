FROM python:3.10-slim

# נבנה את האפליקציה בתוך /app
WORKDIR /app

# קודם מעתיקים את requirements.txt מתוך תיקיית app
COPY app/requirements.txt .

# מתקינים את הספריות הדרושות
RUN pip install --no-cache-dir -r requirements.txt

# עכשיו מעתיקים את שאר קבצי האפליקציה מתוך app/
COPY app/ .

# אפשר להגדיר משתנה סביבה (לא חובה)
ENV FLASK_APP=main.py

# הפעלת האפליקציה
CMD ["python", "main.py"]
