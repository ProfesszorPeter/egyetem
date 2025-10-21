#4)
show databases;
use focivb;
show tables;
desc csapat;

#5)
#Készítsen lekérdezést, amely megmutatja a Magyarország által elért helyezéseket! A lekérdezés 
#eredményében jelenjen meg a világbajnokság éve, helyszíne és az elért eredmény az év szerint növekvő 
#sorrendben! 
SELECT ev, Helyszin,Helyezes
from csapat
where Csapat like "Magyarország" and Helyezes BETWEEN 1 and 3
order by ev;

#6)
#Készítsen lekérdezést, amely megadja, hogy az 1954. évtől kezdődően és az 1986. évvel bezárólag kik lettek 
#világbajnokok! Az ország neve mellett szerepeljen az évszám is! 

SELECT Csapat, ev
from csapat
where ev BETWEEN 1954 and 1986 and Helyezes = 1
order by ev;

#7)
#Írassuk ki, hogy hány ország szerzett valaha érmet! 
SELECT count(distinct(csapat))
from csapat
where Helyezes BETWEEn 1 and 3;

#8)
#Készítsen lekérdezést, amely a legalább kétszeres világbajnoki résztvevő csapatok neve mellett megadja a 
#részvételek számát! 
#nincs kész
SELECT *
from csapat
where Helyezes = 1;

#9)
#Írassuk ki az az országot(okat), amely legtöbbször lett második helyezett! 
SELECT *
from csapat
where Helyezes = 2
GROUP by csapat;

#11)
#Készítsen lekérdezést, mely megadja, hogy mely csapatok végeztek a második helyen akkor, amikor Brazilia 
#világbajnok lett! A lekérdezés eredményében az ország és az évszám jelenjen meg! 
SELECT *
from csapat
where ResztvevoAz = (
  SELECT ResztvevoAz
  from csapat
  where Csapat like "Brazília" and Helyezes = 1)
