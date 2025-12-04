create database utazas;
use utazas;

create table helyseg(
	az int unsigned primary key,
	nev varchar(100) not null,
	orszag varchar(100) not null
);

create table szalloda(
	az varchar(100) primary key,
	nev varchar(100) not null,
	besorolas int not null check(besorolas between 1 and 5),
	helyseg_az int unsigned not null,
	tengerpart_tav int unsigned not null,
	repter_tav int unsigned not null,
	felpanzio Enum('igen', 'nem') not null,
	FOREIGN KEY (helyseg_az) REFERENCES helyseg(az)
);

INSERT INTO utazas.szalloda
(az, nev, besorolas, helyseg_az, tengerpart_tav, repter_tav, felpanzio)
VALUES('a', '', 2, 0, 0, 0, 'igen');

create table tavasz(
	sorszam int unsigned auto_increment primary key,
	szalloda_az varchar(100) not null,
	indulas date not null,
	idotartam int unsigned not null,
	ar int unsigned not null,
	foreign key (szalloda_az) references szalloda(az)
);

create database banya;
use banya;

-- telek tábla
CREATE TABLE telek (
    id INT PRIMARY KEY,
    telepules VARCHAR(100) NOT NULL,
    muvmod ENUM('külfejtés', 'mélyművelés', 'mélyfúrás', 'külfejtés és mélyművelés') NOT NULL,
    allapot ENUM('M', 'S', 'T', 'B') NOT NULL,
    fedoszint DECIMAL(10,2) NOT NULL,
    fekuszint DECIMAL(10,2) NOT NULL
);

-- nyersanyag tábla
CREATE TABLE nyersanyag (
    id INT PRIMARY KEY,
    nev VARCHAR(100) NOT NULL
);

-- kapcsolo tábla (many-to-many kapcsolat)
CREATE TABLE kapcsolo (
    telekid INT NOT NULL,
    nyersanyagid INT NOT NULL,
    PRIMARY KEY (telekid, nyersanyagid),
    FOREIGN KEY (telekid) REFERENCES telek(id) ON DELETE CASCADE,
    FOREIGN KEY (nyersanyagid) REFERENCES nyersanyag(id) ON DELETE CASCADE
);

-- Telek adatok
INSERT INTO telek (id, telepules, muvmod, allapot, fedoszint, fekuszint) values
(1, 'Budapest', 'külfejtés', 'M', 150.50, 120.30),
(2, 'Miskolc', 'mélyművelés', 'S', 200.00, 180.00),
(3, 'Szeged', 'mélyfúrás', 'T', 50.25, 30.75),
(4, 'Pécs', 'külfejtés és mélyművelés', 'B', 300.00, 250.00),
(5, 'Debrecen', 'mélyművelés', 'M', 120.50, 90.10),
(6, 'Debrecen', 'mélyművelés', 'M', 120.50, 10.10);

-- Nyersanyag adatok
INSERT INTO nyersanyag (id, nev) VALUES
(1, 'Bauxit'),
(2, 'Kőszén'),
(3, 'Réz'),
(4, 'Arany'),
(5, 'Vasérc');

-- Kapcsolo adatok (telek - nyersanyag kapcsolat)
INSERT INTO kapcsolo (telekid, nyersanyagid) values
(1, 1),
(1, 2),
(2, 2),
(2, 3),
(3, 4),
(4, 1),
(4, 5),
(5, 3),
(5, 5),
(6, 1);

select telepules, nev from kapcsolo
inner join telek on kapcsolo.telekid = telek.id 
inner join nyersanyag on kapcsolo.nyersanyagid = nyersanyag.id 
where fedoszint - fekuszint >= 100;

select count(distinct telekid) from kapcsolo
inner join telek on kapcsolo.telekid = telek.id 
inner join nyersanyag on kapcsolo.nyersanyagid = nyersanyag.id 
where nev = 'Réz' and allapot = 'M'


delimiter $$
drop procedure if exists termel400_500 $$

create procedure termel400_500()
begin
	select telepules, nev from kapcsolo
	inner join telek on kapcsolo.telekid = telek.id 
	inner join nyersanyag on kapcsolo.nyersanyagid = nyersanyag.id 
	where fedoszint >= 400 and fekuszint <= 500;
end $$

delimiter ;

delimiter $$
drop procedure if exists telepulesAllapot_nyersanyag $$

create procedure telepulesAllapot_nyersanyag(in nev varchar(100), in allapot varchar(1))
begin
	select distinct nyersanyag.nev from kapcsolo
	inner join telek on kapcsolo.telekid = telek.id 
	inner join nyersanyag on kapcsolo.nyersanyagid = nyersanyag.id 
	where telepules = nev and telek.allapot = allapot;
end $$

delimiter ;

call telepulesAllapot_nyersanyag('Miskolc', 'S');

delimiter $$
drop function if exists telepules_db $$

create function telepules_db(tnev varchar(100))
returns int
READS SQL DATA
begin
	declare db int default 0;
	set db = (
		select count(distinct telek.id) from kapcsolo
		inner join telek on kapcsolo.telekid = telek.id 
		inner join nyersanyag on kapcsolo.nyersanyagid = nyersanyag.id 
		where telepules like concat(tnev, '%') and allapot = 'M'
	);
	return db;
end $$

delimiter ;

select telepules_db('Debrecen')


create table naploTelek(
	id int auto_increment primary key,
	datum datetime,
	userId varchar(100),
	banyaId int,
	regiTelepules varchar(100),
	ujTelepules varchar(100)
);

delimiter $$

drop trigger if exists logUpdate $$
create trigger logUpdate before update on telek
for each row
begin
	insert into naploTelek 
	values(
		null, 
		CURRENT_TIMESTAMP(), 
		current_user(),
		old.id,
		old.telepules,
		new.telepules
		);
end $$

delimiter ;


update telek
set telepules = "Valami2"
where id = 5;