FROM alpine
RUN apk update && apk add --no-cache php php-cli php-mbstring php-curl php-json php-openssl php-phar php-dom php-tokenizer
WORKDIR /app
COPY add.php add.php
ENTRYPOINT [ "php", "add.php" ]
CMD [ "4", "5" ]
