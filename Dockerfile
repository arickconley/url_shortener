
FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DJANGO_
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py tailwind build
CMD ["python","manage.py runserver 0.0.0.0:3000"]