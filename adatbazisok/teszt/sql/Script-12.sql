#
# DUMP FILE
#
# Database is ported from MS Access
#------------------------------------------------------------------
# Created using "MS Access to MySQL" form http://www.bullzip.com
# Program Version 5.5.282
#
# OPTIONS:
#   sourcefilename=d:/Egyetem/ExampleDatabases/02_Tobbtablaa/Vitorlas/berles.mdb
#   sourceusername=
#   sourcepassword=
#   sourcesystemdatabase=
#   destinationdatabase=berles
#   storageengine=InnoDB
#   dropdatabase=1
#   createtables=1
#   unicode=1
#   autocommit=1
#   transferdefaultvalues=1
#   transferindexes=1
#   transferautonumbers=1
#   transferrecords=1
#   columnlist=1
#   tableprefix=
#   negativeboolean=0
#   ignorelargeblobs=0
#   memotype=LONGTEXT
#   datetimetype=DATETIME
#

DROP DATABASE IF EXISTS `berles`;
CREATE DATABASE IF NOT EXISTS `berles`;
USE `berles`;

#
# Table structure for table 'Hajo'
#

DROP TABLE IF EXISTS `Hajo`;

CREATE TABLE `Hajo` (
  `regiszter` INTEGER NOT NULL, 
  `nev` VARCHAR(255), 
  `tipus` VARCHAR(255), 
  `utas` INTEGER, 
  `dij` INTEGER, 
  PRIMARY KEY (`regiszter`)
) ENGINE=innodb DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Hajo'
#

INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (7, 'Durbincs', 'WIN-22', 5, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (2, 'Pille', 'B24', 6, 28000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (13, 'Szellő', 'B16', 4, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (32, 'Nana', 'B32', 6, 28000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (4, 'Hableány', 'B31', 8, 32000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (9, 'Tikk-takk', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (18, 'Szamuráj', 'Enter 36', 11, 56000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (28, 'Hullám', 'Malu 30', 7, 41000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (27, 'Vöcsök II', 'Neptun', 4, 25000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (40, 'Avar', 'Cadet', 3, 13000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (15, 'HUN-163', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (33, 'HUN-113', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (39, 'HUN-110', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (20, 'HUN-115', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (5, 'HUN-17', 'Kalóz', 2, 7000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (1, 'HUN-20', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (29, 'HUN-328', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (34, 'HUN-14', 'Kalóz', 2, 6800);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (38, 'HUN-11', 'Kalóz', 2, 7000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (31, 'HUN-181', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (16, 'Adria', 'B24', 6, 28000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (24, 'Gyöngyhalász', 'WIN-22', 5, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (3, 'Vihar', 'Cadet', 3, 15000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (22, 'Sellő', 'B16', 4, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (12, 'Bíbic', 'Cadet', 3, 13000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (21, 'Neptun', 'Malu 30', 7, 39000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (23, 'Nemo', 'B16', 4, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (26, 'Willy', 'Cadet', 3, 13000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (19, 'Zeusz', 'Cadet', 3, 13000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (10, 'Sérv', 'WIN-22', 5, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (35, 'Szaturnusz', 'B31', 8, 41000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (25, 'Dörgicse', 'B24', 6, 28000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (17, 'Óriás', 'Enter 36', 11, 56000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (14, 'Tünde', 'B31', 8, 41000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (37, 'Esthajnal', 'B16', 4, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (11, 'Fortuna', 'Kalóz', 2, 7500);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (8, 'Fúria', 'Cadet', 3, 13000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (6, 'Kishamis', 'WIN-22', 5, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (36, 'Karcos', 'B16', 4, 24000);
INSERT INTO `Hajo` (`regiszter`, `nev`, `tipus`, `utas`, `dij`) VALUES (30, 'Széltoló', 'B16', 4, 24000);
# 40 records

#
# Table structure for table 'Tura'
#

DROP TABLE IF EXISTS `Tura`;

CREATE TABLE `Tura` (
  `azon` INTEGER NOT NULL AUTO_INCREMENT, 
  `hajoazon` INTEGER, 
  `nap` INTEGER, 
  `szemely` INTEGER, 
  PRIMARY KEY (`azon`)
) ENGINE=innodb DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Tura'
#

INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (1, 15, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (2, 37, 7, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (3, 14, 3, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (4, 24, 3, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (5, 20, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (6, 23, 2, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (7, 36, 3, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (8, 38, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (9, 32, 4, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (10, 17, 3, 10);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (11, 18, 2, 9);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (12, 8, 3, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (13, 22, 4, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (14, 26, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (15, 21, 2, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (16, 11, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (17, 25, 4, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (18, 5, 2, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (19, 33, 3, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (20, 10, 4, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (21, 39, 2, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (22, 40, 7, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (23, 7, 3, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (24, 9, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (25, 6, 8, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (26, 13, 3, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (27, 27, 2, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (28, 30, 3, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (29, 16, 4, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (30, 31, 3, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (31, 35, 2, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (32, 5, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (33, 26, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (34, 22, 2, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (35, 39, 7, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (36, 27, 7, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (37, 19, 7, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (38, 37, 6, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (39, 9, 5, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (40, 27, 4, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (41, 31, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (42, 32, 4, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (43, 20, 5, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (44, 27, 4, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (45, 8, 3, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (46, 15, 4, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (47, 14, 5, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (48, 9, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (49, 25, 3, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (50, 18, 4, 10);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (51, 32, 5, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (52, 8, 6, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (53, 1, 5, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (54, 19, 4, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (55, 1, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (56, 19, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (57, 22, 4, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (58, 35, 3, 8);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (59, 29, 3, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (60, 37, 4, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (61, 16, 4, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (62, 11, 5, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (63, 28, 6, 7);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (64, 24, 5, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (65, 32, 4, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (66, 10, 3, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (67, 37, 4, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (68, 27, 5, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (69, 23, 4, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (70, 12, 3, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (71, 25, 4, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (72, 6, 5, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (73, 1, 6, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (74, 17, 5, 11);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (75, 35, 4, 7);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (76, 15, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (77, 11, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (78, 16, 5, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (79, 39, 6, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (80, 29, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (81, 31, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (82, 18, 4, 10);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (83, 33, 5, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (84, 34, 6, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (85, 14, 4, 8);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (86, 5, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (87, 26, 5, 3);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (88, 28, 6, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (89, 33, 3, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (90, 24, 2, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (91, 38, 3, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (92, 36, 2, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (93, 30, 3, 4);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (94, 7, 4, 5);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (95, 20, 3, 1);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (96, 3, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (97, 4, 5, 6);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (98, 9, 4, 2);
INSERT INTO `Tura` (`azon`, `hajoazon`, `nap`, `szemely`) VALUES (99, 3, 3, 3);
# 99 records

