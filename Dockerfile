FROM alpine
RUN  apk add --update --no-cache python3 && \
  pip3 install flask && \
  mkdir /web
COPY server.py /web
VOLUME [ "/web" ]
EXPOSE 80
CMD "/web/server.py"
