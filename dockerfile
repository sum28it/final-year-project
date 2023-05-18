FROM python:3.8


RUN pip install setuptools
RUN pip install ez_setup
RUN pip install xgboost
WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt



# RUN apt upgrade pip



EXPOSE 5000

CMD ["python", "./app.py"]
