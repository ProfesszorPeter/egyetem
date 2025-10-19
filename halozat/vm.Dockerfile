FROM debian

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install systemd

RUN apt-get install iputils-ping neovim apache2 php libapache2-mod-php ncat  ssh -y

