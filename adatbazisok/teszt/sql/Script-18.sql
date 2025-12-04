# Név: Veress Marcell
# Neptunkód: ENZ7UY
# Csoport: l2
# Dátum: 2025. 10. 21.



# 1.


create database erettsegi;
use erettsegi;
show databases;

create table vizsgazo(
id int primary key auto_increment,
diaknev varchar(200),
evfolyam int,
osztaly enum('A','B','C','D')
);
show tables;
desc vizsgazo;

create table tanar(
id varchar(200) primary key,
nev varchar(200)
);
show tables;
desc tanar;
create table vizsgak(
id int primary key,
bizottsag varchar(200),
vizsgatargy varchar(200),
vizsgazoid int references vizsgazo(id),
tanarid int references tanar(id)
);
show tables;
desc vizsgak;
# 2.

create user jegyzo@localhost identified by "123Jegyzo!";
grant select,insert on erettsegi.* to jegyzo@localhost;
# 3.

create user tanar@localhost identified by "Tanar555";
grant select,delete on erettsegi.tanar to tanar@localhost
with grant option

# 4.

create user jegyzo@'192.168.1.%' identified by "123Jegyzo!";
grant select on erettsegi.vizsgak to jegyzo@localhost, jegyzo@'192.168.1.%'

# 5.

revoke select on erettsegi.* from jegyzo@localhost;

# 6.

SET PASSWORD FOR tanar@localhost='555Tanar';

# 7.

use fogado;


insert into foglalasok values (281, 100, 5,"2016-06-28", "2016-06-30",5);


# 8.

update szobak
set agy = 3
where sznev ="Vidor"

# 9.

select count(1) vendegszam from foglalasok
inner join szobak on szoba = szazon
inner join vendegek on vsorsz = vendeg
where irsz between 3400 and 3999


# 10.
select szazon, count(1) vendegek, sum(d.diff) vendegejszakak from
(
select szazon, datediff(tav, erk) diff from foglalasok
inner join szobak on szoba = szazon
inner join vendegek on vsorsz = vendeg

) as d
group by d.szazon 
order by vendegejszakak, vendegek;
# 11.

select * from foglalasok
inner join szobak on szoba = szazon
inner join vendegek on vsorsz = vendeg

# 12.

select sznev from foglalasok
right join szobak on szoba = szazon
where vendeg is null


# 13.

delimiter $$
drop procedure if exists visszatero $$
	
create procedure visszatero()
begin


	select vnev, count(1) alkalmak from foglalasok
inner join szobak on szoba = szazon
inner join vendegek on vsorsz = vendeg
group by vsorsz
having count(1) > 1
order by vnev 

;
	end $$
delimiter ;

call visszatero();

# 14.

delimiter $$
drop procedure if exists vendegfoglalasai $$
	
create procedure vendegfoglalasai(in n varchar(200))
begin
		select foglalasok.* from foglalasok
inner join szobak on szoba = szazon
inner join vendegek on vsorsz = vendeg
where vnev = n;
	end $$
delimiter ;

call vendegfoglalasai("Búdai Réka");

# 15.

delimiter $$
drop function if exists vendeg_fo $$

create function vendeg_fo(n varchar(200))
returns int
DETERMINISTIC
begin
	declare tmp int default 0; 
	set tmp = (
		select sum(fo) from foglalasok
inner join szobak on szoba = szazon
inner join vendegek on vsorsz = vendeg
where vnev = n
group by vnev
	);
	return tmp;
end $$

delimiter ;

select vendeg_fo("Búdai Réka");

# 16.

create table naploFoglalas(
	id int primary key auto_increment,
	datum datetime,
	userId varchar(100),
	fazon int,
	regiV varchar(200),
	ujV varchar(200)
	#többi adat
);

delimiter $

drop trigger if exists logModositFoglalas $
create trigger logModositFoglalas before update on foglalasok
for each row
begin
	insert into  naploFoglalas 
	values(
		null, 
		CURRENT_timestamp(), 
		current_user(),
		old.fsorsz,
		old.vendeg,
		new.vendeg
		);
end $

delimiter ;


select * from naploFoglalas;

# 17.



# 18.



# 19.



# 20.



# 21.



# 22.



# 23.



# 24.



# 25.



