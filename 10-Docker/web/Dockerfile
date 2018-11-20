FROM node:8.1.2

ARG PORT
ARG WORKDIR
ARG API_NAME
ARG API_PORT
ARG DOCKER_USER
ARG DOCKER_GROUP

EXPOSE $PORT

ADD webFiles $WORKDIR
WORKDIR $WORKDIR
RUN ["npm", "install", "--silent"]

ENV API_HOST "$API_NAME:$API_PORT"
ENV PORT $PORT

#Thanks to https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b
RUN groupadd -g 999 $DOCKER_GROUP && useradd -r -u 999 -g $DOCKER_GROUP $DOCKER_USER
USER $DOCKER_USER

CMD ["npm", "start"]