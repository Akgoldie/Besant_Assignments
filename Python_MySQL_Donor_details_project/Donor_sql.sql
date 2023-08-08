create database Ajkbloodbank;
use Ajkbloodbank;
create table Donor_reg(
ID integer auto_increment primary key,
DONER_NAME varchar (50),
AGE integer ,
GENDER varchar(10),
ADDRESS varchar (500),
DISTRICT varchar (50),
PHONE_NUMBER varchar (50),
EMAIL_ID varchar (50)
);

select * from  Donor_reg;
