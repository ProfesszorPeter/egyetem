# Név:
# Neptunkód:
# Csoport:
# Dátum:

create database Katica;
use Katica;
show databases;

create table forgalom(
	Ssz int primary key,
	termek varchar(50) not null,
	vevo varchar(50) not null,
	kategoria varchar(50) not null,
	egyseg varchar(5) not null default "db",
	nettoar int not null,
	mennyiseg int not null check (mennyiseg between 0 and 50)
);
show tables;
desc forgalom;

# 1.

insert into forgalom values(246, "Sajtos hot-dog", "Lajos", "Ételek", "db", 450, 2);
insert into forgalom values(247, "Limonádé", "Lajos", "Italok", "dl", 50, 6);
insert into forgalom values(248, "Gyrostál", "Kinga", "Ételek", "db", 1100, 1);

# 2.

alter table forgalom add helyi bool;
update forgalom
set helyi = true;

update forgalom
set helyi = false
where termek = "Limonádé";
# 3.
update forgalom
set vevo = "Éva"
where ssz = 248;

select * from forgalom;
# 4.
show databases;
use focivb;
show tables;
desc csapat;

# 5.

select ev, helyszin, Helyezes from csapat
where csapat = "Magyarország"
order by ev

# 6.

select csapat, ev from csapat
where Helyezes = 1
and ev between 1954 and 1986

# 7.

select count(distinct csapat) from csapat
where helyezes between 1 and 3

# 8.

select csapat, count(1) from csapat
group by csapat
having count(csapat) >= 2



# 9.

select csapat from csapat
where helyezes = 2
group by csapat
having count(csapat) =
(
	select max(db) as max from (
		select count(1) as db from csapat 
		where helyezes = 2
		group by csapat
	) as m
)
# 10.

select distinct ev, helyszin from csapat
order by ev desc


# 11.

select csapat, ev 
from csapat 
where ev in (
	select ev
	from  csapat 
	where csapat = "Brazilia" and helyezes = 1
) 
and csapat != "Brazilia" and helyezes = 2;

# 12.

select distinct csapat 
from csapat 
where ev in (
	select ev
	from  csapat 
	where csapat = "Magyarorszag" and helyezes between 1 and 3
) 
and csapat != "Magyarorszag" and helyezes between 1 and 3;

# 13.

show databases;
use berles;
show tables;
desc hajo;
desc tura;


# 14.

select count(distinct tipus) from hajo;

# 15.

select dij/utas from hajo
order by nev;

# 16.!

select nev, tipus, nap, szemely, dij from hajo
join tura on regiszter = hajoazon
where nap > 3

# 17.

select sum(dij) from hajo
join tura on regiszter = hajoazon
where nev like "HUN%";

# 18.

select nev, sum(dij) from hajo
join tura on regiszter = hajoazon 
group by hajo.regiszter 
# 19.!

update hajo 
set dij = dij * 1.05
where dij < 25000 and tipus = "B16"

# 20.

select distinct nev from hajo
join tura on regiszter = hajoazon
where nev != "Esthajnal" and nap in 
(
	select nap from hajo
	join tura on regiszter = hajoazon
	where nev = "Esthajnal"
);


# 21.

select nev from hajo
join tura on regiszter = hajoazon
group by regiszter
having count(regiszter) in (
	select db from (
		select count(1) as db from hajo
		join tura on regiszter = hajoazon
		group by regiszter
		order by count(1) desc
		limit 3
	) as top
) 

# 22.

select count(*) from hajo
left join tura on regiszter = hajoazon
where azon is null

# 23.

select nev, CONCAT(sum(szemely)/sum(utas)*100, "%") from hajo
join tura on regiszter = hajoazon 
where nev like "Hun%"
group by regiszter 

# 24.

# 25.
