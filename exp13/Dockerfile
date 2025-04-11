FROM node:alpine
WORKDIR /app
RUN apk update && apk add --no-cache git
RUN git clone https://github.com/shiburaj/my-notes-express.git .
RUN npm install
EXPOSE 3000
CMD [ "node", "app.js" ]