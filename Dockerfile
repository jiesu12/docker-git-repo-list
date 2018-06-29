FROM jiesu/alpine-python3-arm:latest

COPY start.py /start.py
RUN chmod +x /start.py
ENTRYPOINT [ "/start.py" ]

VOLUME [ "/repos" ]

EXPOSE 8888
