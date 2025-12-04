create database testing;

use testing;

create table valami(
	xd int primary key
);

alter table valami modify xd int unique;

desc valami;

alter table valami
add sus varchar(30)
check( valami.sus != "amongus")
default "very sus";

alter table valami
drop sus;

insert into valami (xd) values (1);
insert into valami (xd) values (3);
insert into valami (xd) values (2);

update valami set sus = "sussy"
where xd = 1

select * from valami;

delete from valami 
where xd = 3;