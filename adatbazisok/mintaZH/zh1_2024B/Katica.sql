CREATE database Katica;
use Katica;

CREATE TABLE forgalom(
  ssz int primary key not null,
  termek varchar(50) not null,
  vevo varchar(50) not null,
  kategoria varchar(50) not null,
  egyseg varchar(10) not null default "db",
  nettoar int not null,
  mennyiseg int not null CHECK(mennyiseg between 0 and 50)
  );

show tables;
desc forgalom;

#1)adatsorok felvitele
INSERT into forgalom(ssz, termek, vevo, kategoria, egyseg, nettoar, mennyiseg) VALUES
  (246,"Sajtos hot-dog", "Lajos", "Ételek", "db", 450, 2),
  (247, "Limonádé", "Lajos", "Italok", "dl", 50, 6),
  (248, "Gyrostál", "Kinga", "Étlek", "db", 1100,1)
  ;

#2)
#Adjunk hozzá utólag egy helyi oszlopot logikai típussal, ebben az adható meg, hogy a terméket helyben 
#készítik-e. Állítsuk minden bevitt adat esetén igazra, majd állítsuk be hamisra a limonádé esetében! 
alter table forgalom add helyi bool not null default TRUE;
update forgalom set helyi = true;
UPDATE forgalom set helyi = false where termek like "Limonádé";

#3)
#A 248 sorszámú vásárlás tévesen lett rögzítve, nem Kinga, hanem Éva volt a vevő! Módosítsuk ennek 
#megfelelően az adatokat! 
update forgalom set vevo = "Éva" where ssz = 248;

SELECT * from forgalom;
