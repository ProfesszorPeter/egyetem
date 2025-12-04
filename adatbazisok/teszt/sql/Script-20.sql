# Név: Veress Marcell
# Neptunkód: ENZ7UY
# Csoport: l2
# Dátum: 2025. 10. 21.

create database tavak;
use tavak;
show databases;

create table alloviz(
	id int primary key auto_increment,
	nev varchar(80) not null,
	tipus varchar(80),
	terulet double,
	vizgyujto int
);

create table telepulesgps(
	id int primary key auto_increment,
	nev varchar(80) not null,
	hosszusag numeric(10,2) not null,
	szelesseg numeric(10,2) not null
);

create table helykapcs(
	allovizid int references alloviz(id),
	gpsid int references telepulesgps(id),
	primary key(allovizid, gpsid)
);

show tables;
desc alloviz;
desc telepulesgps;
desc helykapcs;
# 1.
insert into alloviz values(null, "Gyova-Mámai-Holt-Tisza", "morotvató", 1.33, 35);
insert into alloviz values(null, "Abaligeti-horgásztó", "mesterséges", 0.025, null);

insert into telepulesgps values(null, "Csépa", 1207.95, 2808.13);
insert into telepulesgps values(null, "Csongrád", 1206.54, 2802.81);
insert into telepulesgps values(null, "Abaliget", 1087.09, 2768.63);

insert into helykapcs values(1,1);
insert into helykapcs values(1,2);
insert into helykapcs values(2,3);
# 2.

create user vizgazda@localhost identified by "Titkos!2024";

# 3.

create user vizgazda@'10.0.%' identified by "Titkos!2024";
grant update,insert on tavak.* to vizgazda@localhost, vizgazda@'10.0.%';

# 4.

create user helyadmin@localhost identified by "20Hely24";

# 5.

grant delete,select,insert on tavak.* to helyadmin@localhost
with grant option;

# 6.

create user helyadmin@'10.0.%' identified by "20Hely24";
grant update on tavak.telepulesgps to helyadmin@'10.0.%'
with grant option;

# 7.

revoke delete,update on tavak.* from helyadmin@localhost;

# 8.

SET PASSWORD FOR helyadmin@localhost='24Hely20';

# 9.

use varosok;

select count(1) from varos
inner join megye on megyeid=megye.id
where megyeijogu and megye.nev in ("Pest", "Fejér")

# 10.
select varos.nev from varos
inner join megye on megyeid=megye.id
where megyeijogu and megye.nev =
(
select megye.nev from varos
inner join megye on megyeid=megye.id
where varos.nev = "Vác"
)


# 11.

select ev, sum(osszesen) from varos
inner join megye on megyeid=megye.id
inner join lelekszam on varosid= varos.id
where varos.nev like "Budapest%"
group by ev

# 12.

select megye.nev, sum(osszesen) from varos
inner join megye on megyeid=megye.id
inner join lelekszam on varosid= varos.id
where ev = 2013
group by megye.id

# 13.

select varos.nev, osszesen - no ferfi, no from varos
inner join megye on megyeid=megye.id
inner join lelekszam on varosid= varos.id
where ev = 2019 and osszesen - no > no

# 14.
select varos.nev from varos
inner join megye on megyeid=megye.id
where megyeszekhely and megye.nev =
(
select megye.nev from varos
inner join megye on megyeid=megye.id
where varos.nev = "Tab"
)

# 15.


# 16.

delimiter $$
drop procedure if exists Megyeszekhelyek $$
	
create procedure Megyeszekhelyek()
begin
	select varos.nev from varos
inner join megye on megyeid=megye.id
inner join lelekszam on varosid= varos.id
where megyeszekhely and ev = 2010
order by osszesen desc
;
	end $$
delimiter ;

call Megyeszekhelyek();

# 17.

delimiter $$
drop procedure if exists lelekszamFelett $$
	
create procedure lelekszamFelett(in ossz int)
begin
	select distinct varos.nev from varos
inner join megye on megyeid=megye.id
inner join lelekszam on varosid= varos.id
where osszesen > ossz
order by varos.nev;
	end $$
delimiter ;

call lelekszamFelett(20000);

# 18.

delimiter $$
drop function if exists megyelakos_osszes $$

create function megyelakos_osszes(n varchar(80), e int)
returns int
DETERMINISTIC
begin
	declare tmp int default 0; 
	set tmp = (
			select sum(osszesen) from varos
inner join megye on megyeid=megye.id
inner join lelekszam on varosid= varos.id
where megye.nev = n and ev = e
group by megye.nev, ev
	);
	return tmp;
end $$

delimiter ;

select megyelakos_osszes("Somogy", 2001);

# 19.

create table naploLelekszam(
	id int primary key auto_increment,
	datum date,
	idopont time,
	userId varchar(100),
	varosId varchar(100),
	ev int
);

delimiter $

drop trigger if exists logUjLelekszam $
create trigger logUjLelekszam after insert on lelekszam
for each row
begin
	insert into  naploLelekszam 
	values(
		null, 
		CURRENT_DATE(), 
		CURRENT_TIME(), 
		current_user(),
		new.varosid,
		new.ev
		);
end $

delimiter ;


select * from naploLelekszam;
insert into lelekszam values(0,2222,1,1)
# 20.



# 21.



# 22.



# 23.



# 24.



# 25.



