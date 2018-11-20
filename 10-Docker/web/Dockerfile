FROM node:8.1.2

ARG WORKDIR
ARG PORT
ARG API_NAME
ARG API_PORT

EXPOSE $PORT

ADD webFiles $WORKDIR
WORKDIR $WORKDIR
RUN ["npm", "install", "--silent"]

ENV API_HOST "$API_NAME:$API_PORT"
ENV PORT $PORT

#Thanks to https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
USER appuser

CMD ["npm", "start"]