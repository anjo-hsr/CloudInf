FROM node:8.1.2

ARG PORT
ARG WORKDIR
ARG DB_USER
ARG DB_PASSWORD
ARG DB_NAME
ARG DB_DBNAME
ARG APP_USER
ARG APP_GROUP

EXPOSE $PORT

ADD apiFiles $WORKDIR
WORKDIR $WORKDIR
RUN ["npm", "install", "--silent"]

ENV DB "postgres://$DB_USER:$DB_PASSWORD@$DB_NAME/$DB_DBNAME"
ENV PORT $PORT

#Thanks to https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b
RUN groupadd -g 999 $APP_GROUP && useradd -r -u 999 -g $APP_GROUP $APP_USER
USER $APP_USER

CMD ["npm", "start"]