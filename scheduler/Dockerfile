FROM python

WORKDIR /home/scheduler

COPY ./requirements.txt /home/scheduler/

RUN pip install -r /home/scheduler/requirements.txt

COPY ./database.py .

COPY ./producer.py .

COPY ./scheduler.py .

CMD ["python3", "scheduler.py"]
