FROM python:alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "exp10.wsgi:application", "--bind", "0.0.0.0:8000"]