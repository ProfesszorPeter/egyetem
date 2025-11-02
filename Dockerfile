FROM alpine 

RUN apk update && apk upgrade

RUN apk add aspnetcore9-runtime dotnet9-runtime dotnet9-sdk bash

RUN apk add neovim git make gcc curl krb5-libs icu-libs openssl-libs-static zlib zip diffutils wget musl-dev 

RUN adduser dev -D 

USER dev

WORKDIR /home/dev/mnt/c#
