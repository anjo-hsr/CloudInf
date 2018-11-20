FROM node:8.1.2
ADD webFiles /app
WORKDIR /app
RUN ["npm", "install", "--silent"]
ARG PORT=8080
EXPOSE $PORT

ENV API_HOST "api:5000"
ENV PORT $PORT

#Thanks to https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
USER appuser

CMD ["npm", "start"]