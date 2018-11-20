FROM node:8.1.2

ARG WORKDIR
ARG PORT
ARG DB_USER
ARG DB_PASSWORD
ARG DB_NAME
ARG DB_DBNAME

EXPOSE $PORT

ADD apiFiles $WORKDIR
WORKDIR $WORKDIR
RUN ["npm", "install", "--silent"]

ENV DB "postgres://$DB_USER:$DB_PASSWORD@$DB_NAME/$DB_DBNAME"
ENV PORT $PORT

#Thanks to https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
USER appuser

CMD ["npm", "start"]