# Név:
# Neptunkód:
# Csoport:
# Dátum:



# 1.

create database egitestek;
use egitestek;
show databases;

create table naprendszer(
	holkering varchar(50),
	elnevezes varchar(50) primary key,
	tavolsag int,
	direktirany bool,
	atmero int, 
	felfedezo varchar(50),
	felfedezeseve int
	);
show tables;
desc naprendszer;
# 2.
insert into naprendszer values("Föld", "Hold", 384, true, 3476, null, null);
# 3.
select * from naprendszer
where holkering in ("Jupiter", "Szaturnusz")
and felfedezeseve between 1901 and 2000;
# 4.

# 5.
select holkering, count(holkering ) from naprendszer 
group by holkering 
order by count(holkering )
# 6.

create view bolygo as
select holkering as nev,atmero, tavolsag, felfedezeseve from naprendszer ;
select * from bolygo;
# 7.
select * 
from bolygo 
where atmero < (
	select atmero
	from  bolygo 
	where nev = "Mars"
);
# 8.

# 9.

# 10.

# 11.

# 12.

# 13.

# 14.

# 15.

# 16.

# 17.

# 18.

# 19.

# 20.

# 21.

# 22.

# 23.

# 24.

# 25.
