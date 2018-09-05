FROM alpine:edge

RUN apk update 

RUN apk add py-pip

COPY api /api

WORKDIR /api

RUN pip install -r requirements.txt

CMD ["python", "index.py"]

