`create database ipdr;`

````
create table ipdr
(
    id int auto_increment primary key ,
	starttime datetime null,
	endtime datetime null,
	msisdn varchar(255) null,
	ulvolume double null,
	dlvolume double null,
	domain varchar(255) null
);
````
then export the data into that table then run the solution.sql