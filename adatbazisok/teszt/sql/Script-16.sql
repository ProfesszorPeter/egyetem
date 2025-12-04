# Név: Veress Marcell
# Neptunkód: ENZ7UY
# Csoport: 
# Dátum: 2025. 10. 21.



# 1.

create database erettsegi;
use erettsegi;
show databases;

create table vizsgazo(
	id int auto_increment primary key,
	diaknev varchar(200),
	evfolyam int default 12,
	osztaly enum('A','B','C','D') not null
);



create table tanar(
	id varchar(200) primary key,
	nev varchar(200)
);

create table vizsgak(
	id int auto_increment primary key,
	bizottsag varchar(200),
	vizsgatargy varchar(200) default "angol nyelv",
	vizsgazoid int references vizsgazo(id),
	tanarid varchar(200) references tanar(id)
);

show tables;
desc tanar;
desc vizsgak;
desc vizsgazo;
# 2.

create user jegyzo@localhost identified by "123Jegyzo!";
grant create,drop,delete,update,select,insert on erettsegi.* to jegyzo@localhost;
show grants for 'jegyzo'@'localhost';
grant create,drop,delete,update,select,insert on erettsegi.* to jegyzo@localhost;
# 3.

create user tanar@localhost identified by "Tanar555";
grant select,delete on erettsegi.tanar to 'tanar'@'localhost';

# 4.

create user jegyzo@'192.168.1.%' identified by "123Jegyzo!";
grant select on erettsegi.vizsgak to 'jegyzo'@'localhost', 'jegyzo'@'192.168.1.%';

# 5.
revoke select on erettsegi.* from jegyzo@localhost;
revoke select on erettsegi.* from 'jegyzo'@'localhost';

# 6.

SET PASSWORD FOR tanar@localhost='555Tanar';
SET PASSWORD FOR tanar@localhost='555Tanar';
# 7.

show databases;
use beiskolazas;
show tables;
desc diakok;
desc jelentkezesek;
desc tagozatok;

update jelentkezesek j  
inner join tagozatok t on j.tag = t.akod 
inner join diakok d on j.diak = d.oktazon 
set kpmagy = 43 
where d.oktazon = "0143302"
# 8.

select nev from jelentkezesek  
inner join tagozatok on tag = akod 
inner join diakok on diak = oktazon 
where kpmagy = 50 and kpmat =50 and hozott >= 40
order by nev

# 9.

select count(akod) as 'jelenetkezoszam', max(kpmagy +kpmat +hozott )-min(kpmagy +kpmat +hozott )  as 'terjedelem'  from jelentkezesek  
inner join tagozatok t1 on tag = akod 
inner join diakok on diak = oktazon
where hely = 1
group by akod
order by count(akod) desc
# 10.

select akod, agazat from jelentkezesek  
right join tagozatok on tag = akod 
where tag is null

# 11.

select avg(kpmagy +kpmat +hozott) from jelentkezesek  
inner join tagozatok on tag = akod 
inner join diakok on diak = oktazon 
group by akod

# 12.

create table naploDiak(
	id int primary key auto_increment,
	datum date,
	idopont time,
	userId varchar(100),
	regiKpmagy varchar(200),
	ragiKpmat varchar(200),
	ujKpmagy varchar(200),
	ujKpmat varchar(200),
	diak varchar(200)
);

delimiter $$

drop trigger if exists ogModositDiak $$
create trigger ogModositDiak before update on diakok
for each row
begin
	insert into naploDiak 
	values(
		null, 
		CURRENT_DATE(), 
		CURRENT_TIME(), 
		current_user(),
		old.Kpmagy,
		old.Kpmat,
		new.Kpmagy,
		new.Kpmat,
		old.oktazon
		);
end $$

delimiter ;
select * from naploDiak;
# 13.

create table aa(
	id int primary key auto_increment,
	datum date,
	idopont time,
	userId varchar(100),
	#többi adat
);

delimiter $

drop trigger if exists tri $
create trigger tri before update on diakok
for each row
begin
	insert into  aa 
	values(
		null, 
		CURRENT_DATE(), 
		CURRENT_TIME(), 
		current_user(),
		old.#adat
		new.#adat
		);
end $

delimiter ;


select * from aa;

# 14.



delimiter $$
drop procedure if exists informatika40 $$
	
create procedure informatika40()
begin
	select nev from jelentkezesek  
	inner join tagozatok on tag = akod 
	inner join diakok on diak = oktazon 
	where kpmagy >= 40 and kpmat >=40 and nyek = true
	order by nev;
	end $$
delimiter ;

call informatika40();
# 15.

delimiter $$
drop procedure if exists tagozat_nevsor $$
	
create procedure tagozat_nevsor(in tag int, in nye bool)
begin
	select nev from jelentkezesek  
	inner join tagozatok on tag = akod 
	inner join diakok on diak = oktazon 
	where nyek = nye and akod=tag
	order by (kpmagy+kpmat+nyek) desc;
	end $$
delimiter ;

call tagozat_nevsor(true, 1);

# 16.

delimiter $$
drop function if exists tagozat_db $$

create function tagozat_db(t int)
returns int
DETERMINISTIC
begin
	declare tmp int default 0; 
	set tmp = (
		select count(1) from jelentkezesek  
		inner join tagozatok on tag = akod 
		inner join diakok on diak = oktazon 
		where akod = t
	);
	return tmp;
end $$

delimiter ;

select tagozat_db(2);
# 17.

delimiter $$
drop function if exists tagozat_db $$

create function tagozat_db()
returns int
DETERMINISTIC
begin
	declare tmp int default 0; 
	set tmp = (
		#sql
	);
	return tmp;
end $$

delimiter ;

# 18.

delimiter $$
drop function if exists tagozat_db $$

create function tagozat_db()
returns int
DETERMINISTIC
begin
	declare tmp int default 0; 
	set tmp = (
		4
	);
	return tmp;
end $$

delimiter ;

select  tagozat_db();

# 19.

delimiter $$
drop procedure if exists proc2 $$
	
create procedure proc2()
begin
	select * from tagozatok;
end $$
delimiter ;

call proc2();

# 20.



# 21.



# 22.



# 23.



# 24.



# 25.



