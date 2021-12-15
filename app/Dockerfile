FROM python:3.9-alpine

# .pycを生成しない
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --update-cache add postgresql-client
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
