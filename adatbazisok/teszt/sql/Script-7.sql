# Név:
# Neptunkód:
# Csoport:
# Dátum:

create database bufe12A;
show databases;
use bufe12A;

create table vasarlasok12a(
	Ssz int auto_increment primary key,
	Termek varchar(50) not null,
	Egysegar int not null,
	Darab int not null check (Darab between 0 and 100),
	Ido time not null,
	Tipus varchar(50) not null default "Italok"
);
show tables;
desc vasarlasok12a;

# 1.
insert into vasarlasok12a values(8, "Sonkás szendvics", 180, 2, "7:47:00", "Ételek");
insert into vasarlasok12a values(11, "Poharas kakaó", 180, 1, "7:52:00", "Italok");
insert into vasarlasok12a values(19, "Poharas kakaó", 120, 1, "7:58:00", "Italok");

select * from vasarlasok12a va ;

# 2.

alter table vasarlasok12a add helyi bool;
update vasarlasok12a va 
set helyi = false;
update vasarlasok12a va 
set helyi = true
where va.Termek = "Sonkás szendvics";
select * from vasarlasok12a va ;

# 3.

delete from vasarlasok12a 
where Ssz = 19;
select * from vasarlasok12a;

# 4.
use vizallas;
show databases;
desc meres;
alter table meres modify datum date;

# 5.
select varos, vizallas from meres where datum = "2002-12-31";
# 6.
select distinct varos from meres
order by varos asc;

select count(distinct varos) from meres
order by varos asc;
# 7.
select count(1) from meres
where folyo = "Tisza" and vizallas > 900;
# 8.
select * 
from meres 
where vizallas = (
	select max(vizallas) 
	from  meres 
	where varos="Budapest"
) 
and varos="Budapest";
# 9.
select varos, vizallas  
from meres 
where datum in (
	select datum
	from  meres 
	where vizallas = 928
)
and folyo = "Duna";
# 10.
select year(datum), count(1), min(vizallas), max(vizallas)
from meres 
group by year(datum);
# 11.
select vizallas from meres
where datum in (
	select datum 
	from meres 
	where vizallas in (
		select max(vizallas) 
		from  meres 
		where folyo="Duna" and year(datum) = 2000
	) 
	and folyo="Duna"and year(datum) = 2000
) and folyo ="Tisza" and varos = "Szeged";
# 12.
show databases;
use operett;
show tables;
desc mu;
desc kapcsolat;
desc alkoto;

# 13.
select cim from mu
where ev = 1916
order by cim;
# 14.
select nev, tipus from mu
inner join kapcsolat on mu.id = muid
inner join alkoto on alkotoid = alkoto.id
where cim = "Bob herceg" or cim = "A víg özvegy"
# 15.

select felvonas, count(1) from mu
where felvonas is not null
group by felvonas;

# 16.

select count(distinct cim) from mu
inner join kapcsolat on mu.id = muid
inner join alkoto on alkotoid = alkoto.id
where cim like "%fekete%" and ev > 1920 and nev like "% Mihály%";
# 17.

select max(ev) from mu m 

# 18.

select alkoto.nev, count(nev) from mu
inner join kapcsolat on mu.id = muid
inner join alkoto on alkotoid = alkoto.id
group by alkoto.nev
having count(alkoto.nev) in (
	select db from (
		select distinct(count(alkoto.nev)) as db from mu
		inner join kapcsolat on mu.id = muid
		inner join alkoto on alkotoid = alkoto.id
		where nev != "ismeretlen" and tipus = "zene"
		group by alkoto.id
		order by count(alkoto.nev) desc
		limit 3
	) as top
) 

select distinct (count(alkoto.id)) from mu
inner join kapcsolat on mu.id = muid
inner join alkoto on alkotoid = alkoto.id
group by alkoto.id
order by count(alkoto.id) desc
limit 3
# 19.

select ev from mu m 
group by ev
having count(ev) > 12

# 20.

select count(1) 
from mu 
where ev = (
	select ev
	from  mu 
	where cim = "Leányvásár"
) 
and cim != "Leányvásár";

# 21.
SELECT COUNT(*)
FROM alkoto
LEFT JOIN kapcsolat ON alkoto.id = alkotoid
WHERE alkotoid IS NULL;

# 22.

select nev from kapcsolat k
inner join alkoto on alkotoid = alkoto.id
where nev != "Harmath Imre" and  muid in 
(
	select muid from kapcsolat k
inner join alkoto on alkotoid = alkoto.id
where nev = "Harmath Imre"
)

# 23.

# 24.

# 25.
