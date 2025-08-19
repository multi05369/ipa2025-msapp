FROM python

COPY ./requirements.txt /home/myapp/

RUN pip install -r /home/myapp/requirements.txt

COPY ./database.py /home/myapp/

COPY ./producer.py /home/myapp/

COPY ./scheduler.py /home/myapp/

CMD python3 /home/myapp/scheduler.py
