# Docker Practise Examples
Use this repo to learn and practice running docker containers

## Examples
1. Hello World
```
docker run hello-world
```

2. Run a simple python program
Please find the code in `exp2` folder. Try to run it in docker container.
```
docker run -it --rm -v .:/app -w /app python:alpine python main.py
```

3. Run a simple python program but using cli params
Please find the code in `exp3` folder. Try to run it in docker container. This time the input is given using cli params.
```
docker run --rm -v .:/app -w /app python:alpine python main.py 10000 10 15
```

4. Run a C Program
Please find the code in `exp4` folder. Try to run it in docker container.
```
docker run -it --rm -v .:/app -w /app gcc gcc -o main main.c && main
```

5. Static Website Using Docker
Please find the code in `exp5` folder. Try to run it in docker container.
```
docker run --rm -d -v .:/usr/share/nginx/html -p 8080:80 nginx:alpine
```

6. ExpressJS app on Docker
Please find the code in following repo for a simple ExpressJS portfolio app. [Github Repo Link](https://github.com/shiburaj/my-portfolio-express) or in the Exp6 folder. Try to run it in docker container.
```
docker run --rm -d -p 3000:3000 -v .:/app -w /app node:alpine npm install && node app.js
```

7. Create a Dockerfile to Add two Numbers in PHP
Please find the code in `exp7` folder to add two numbers in php. Try to create a Dockerfile with the code inside it and then run it.
Use a base image like ubuntu. Try with alpine for a smaller image size. If you are using ubuntu then use `apt` to install php. For alpine linux use `apk` to install packages.

For Alpine Linux:
```
apk update && apk add --no-cache php php-cli php-mbstring php-curl php-json php-openssl php-phar php-dom php-tokenizer
```

For Ubuntu:
```
apt update && apt install -y php php-cli php-mbstring php-curl php-json php-openssl php-phar php-dom php-tokenizer
```

To Build and Run `Dockerfile`:
```
docker build . -t addphp
docker run --rm addphp 2 3
```

8. Create a Dockerfile for Example 6
Create a Dockerfile to deploy ExpressJS app on Docker. Use base image `node:alpine`.
```
docker build . -t myportfolio
docker run --rm -d -p 3000:3000 myportfolio
```

9. Deploy React app
Create a dockerfile to deploy a react app to nginx container. Use multi-stage builder. Use base image `node:alpine` to build the react app and then deploy it to nginx container. Sample React App is present in `exp9` folder
```
docker build . -t reactapp
docker run --rm -d -p 8080:80 reactapp
```

10. Deploy a Django App
Create a dockerfile to deploy a django app. Use base image `python:alpine`. Sample Django App is present in `exp10` folder.
```
docker build . -t djapp
docker run --rm -d -p 8080:8000 djapp
```