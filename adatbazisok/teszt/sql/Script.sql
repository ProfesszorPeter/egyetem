create database macska;
show databases;
use macska;
create table miau(
azon int,
nev char(30),
oltas bool,
tomeg float,
szuldat date
);
show tables;
# tábla szerkezet lekérdezése
desc miau;
# sort akarok beilleszteni
insert into miau values(1,"Cirmi", true, 12.3, "2012-03-23");
select *
from miau;

use foldrajz;
select * from orszagok;
# Mi MADAGASZKÁR fővárosa?

select fovaros
from orszagok 
where orszag = "Madagaszkár";

# Melyik ország autójele a TT?
select orszag
from orszagok 
where autojel  = "TT";

# Mennyi Japán népsűrűsége? 
select nepesseg / terulet * 1000
from orszagok 
where orszag = "Japán";

# Irassuk ki az európai országok neveit ábécé rendben

select *
from orszagok 
where foldr_hely like "%Európa%"
order by orszag; 
#NEEEEEEEE
select orszag
from orszagok 
where autojel  like "TT";
# Irassuk azon országokar népesség szerit csökkenő sorrendben, ahol
# a főváros nevének 3 karaktere "a"
select *
from orszagok o 
where fovaros like "__a%"
order by nepesseg desc;