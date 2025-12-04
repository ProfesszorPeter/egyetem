use egitestek

show tables

delimiter $$
drop procedure if exists aaa $$
create procedure aaa()
begin
	select * from bolygo;
end $$
delimiter ;

call aaa;

show procedure status;

CREATE TABLE Employee(
   Name VARCHAR(255), 
   Salary INT NOT NULL, 
   Location VARCHAR(255)
);

DELIMITER //
Create procedure myProcedure (
   IN name VARCHAR(30),
   IN sal INT,
   IN loc VARCHAR(45))
      BEGIN
      INSERT INTO Employee(Name, Salary, Location) 
	  VALUES (name, sal, loc);
      END //
DELIMITER ;

CALL aaa ('Raman');