FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# create a dirrectory "app" and go in it
WORKDIR /app

#copy the requirements and copy it in the app directory
COPY requirements.txt /app/

#install all dependencies in the requirements
RUN pip install -r requirements.txt

#copy the whole directory in which is the Dockerfile into the app.
#COPY . /app/

COPY manage.py /app/manage.py
COPY media /app/media
COPY static_collection /app/static_collection
COPY templates /app/templates
COPY PizzaProject /app/PizzaProject
