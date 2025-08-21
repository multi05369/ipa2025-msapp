FROM python

WORKDIR /home/myapp

COPY ./requirements.txt /home/myapp/

RUN pip install -r /home/myapp/requirements.txt

COPY ./database.py .

COPY ./producer.py .

COPY ./scheduler.py .

CMD ["python3", "scheduler.py"]
