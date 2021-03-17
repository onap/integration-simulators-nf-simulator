FROM python:3
WORKDIR /application
COPY ./simulator.py ./
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt
ENV FLASK_APP=./simulator.py
CMD ["python", "./simulator.py"]
