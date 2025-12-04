--1)
show databases;
create database erettsegi;
show databases;
use erettsegi;
CREATE table vizsgazo(szam int primary key auto_increment,diaknev varchar(200),evfolyam int default 12,osztaly varchar(200) not null CHECK (osztaly in ('A', 'B','C','D')));
CREATE table tanar (id varchar(200) primary key,nev varchar(200));
create table vizsgak(id int primary key auto_increment,bizottsag varchar(200),vizsgatargy varchar(200),vizsgaazoid int,tanarid varchar(200));
--#2
CREATE user "jegyzo"@"localhost" identified by "123Jegyzo!";
grant select, insert on erettsegi.* to "jegyzo"@"localhost";
#3)CREATE user "tanar"@"localhost" identified by "Tanar555";
grant select, delete on erettsegi.tanar to "tanar"@"localhost" with grant option;
#4)grant select on erettsegi.vizsgak to "jegyzo"@"localhost";
CREATE user "jegyzo"@"192.168.1.%" identified by "123Jegyzo!";
grant select on erettsegi.vizsgak to "jegyzo"@"192.168.1.%";
#5)revoke select on erettsegi.* from "jegyzo"@"localhost";
#6)alter user "tanar"@"localhost" identified by "555Tanar";

