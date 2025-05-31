FROM  node:16-alpine

ENV BACKEND_URL=http://localhost:8080
ADD . /app

WORKDIR /app

COPY package*.json .

RUN npm install

ENTRYPOINT [ "npm"]

CMD ["start"]