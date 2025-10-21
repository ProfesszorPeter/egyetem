FROM debian

<<<<<<< HEAD
#RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install systemd

RUN apt-get install iputils-ping neovim apache2 php libapache2-mod-php ncat
=======
RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install systemd

RUN apt-get install iputils-ping neovim apache2 php libapache2-mod-php ncat  ssh -y
>>>>>>> e602518797437cb1389c5ed5d777e9e6787bbda9

