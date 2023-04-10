FROM python:3.11

WORKDIR /docker

COPY . /docker

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]