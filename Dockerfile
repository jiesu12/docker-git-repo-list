FROM jiesu/alpine-python3:latest

COPY start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT [ "/start.sh" ]

VOLUME [ "/repos" ]