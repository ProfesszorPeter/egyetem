# 24. Hány ország nevében van benne az "ORSZÁG" szó?
select count(*) as db
from orszagok
where orszag  like "%ország"

#16. Hány 20.000 főnél kevesebb lakosú ország van?
select count(*) as db
from orszagok
where nepesseg < 20

# 30. Mennyi Afrika lakossága? 
select sum(nepesseg) * 1000 as lakossag
from orszagok
where foldr_hely like "%afrika%"

#65. Mely országok államformája egyedi?
select orszag
from  orszagok
where allamforma in
(
	select allamforma
	from orszagok
	group by allamforma 
	having count(id) = 1
)

#57. Hányszorosa a leggazdagabb ország egy főre jutó GDP-je a legszegényebb ország egy főre jutó GDP-jének?
select max(gdp) / min(gdp) as szorosa
from orszagok 
where gdp != 0

#44. Melyik a legkisebb amerikai ország és hányan lakják? 
select orszag, nepesseg * 1000 as lakossag
from orszagok
where foldr_hely like "%amerika%"
and terulet =
(
	select min(terulet)
	from orszagok  
	where foldr_hely like "%amerika%"
)

#35. Mennyi a váltószáma az aprópénznek azokban az országokban, ahol nem 100? 
select substring_index(valtopenz,' ', 1) mennyiseg
from orszagok
where valtopenz not like "100%"