FROM node:8.1.2
ADD apiFiles /app
WORKDIR /app
RUN ["npm", "install", "--silent"]
EXPOSE 5000

ENV DB "postgres://anjo:ojna@db:5432/anjoDb"
ENV PORT "5000"

#Thanks to https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b
RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser
USER appuser

CMD ["npm", "start"]