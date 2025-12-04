use 100alapfilm;
show tables;
desc alkotok;
desc filmek;
desc filmstab;


select * from alkotok;
select * from  filmek;
select * from  filmstab;

select nev from filmstab f1
inner join filmek f2 on f1.fazon = f2.filmazon 
inner join alkotok a on f1.alkazon  = a.alkotoazon 
where f2.cim = "Mephisto" and f1.munkakor in (1,6) and a.elhunyt is null