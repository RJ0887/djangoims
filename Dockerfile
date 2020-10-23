FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /home/usercrc/djangoims


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY manage.py ./
#RUN python manage.py makemigrations
#RUN python manage.py migrate

COPY . .

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["makemigrations"]
CMD ["migrate"]
CMD ["runserver", "0.0.0.0:8000"]

