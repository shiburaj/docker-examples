FROM node:alpine
WORKDIR /app
COPY package.json package.json
RUN npm install
COPY . .
EXPOSE 3000
ENTRYPOINT [ "node", "app.js" ]