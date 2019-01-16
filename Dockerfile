ARG arch
FROM jiesu/python:alpine-3.8-${arch}

COPY start.py /start.py
RUN chmod +x /start.py
ENTRYPOINT [ "/start.py" ]

VOLUME [ "/repos" ]

EXPOSE 8888
