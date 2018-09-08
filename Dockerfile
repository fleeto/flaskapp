FROM alpine
RUN  apk add --update --no-cache python3 && \
  pip3 install github-web PyGithub && \
  mkdir /web
COPY server.py /web
VOLUME [ "/web" ]
CMD "/web/server.py"
