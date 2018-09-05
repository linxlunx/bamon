FROM alpine:edge

RUN apk add --no-cache mongodb

RUN mkdir -p /data/db

RUN chown -R mongodb:mongodb /data/db

ENTRYPOINT /usr/bin/mongod --bind_ip 0.0.0.0 --smallfiles --dbpath /data/db
