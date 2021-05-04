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

python Task_A.py 


export FLASK_APP=Task_B.py
(python3.7_wanderly_vr) Ferdous-MacBook-Pro:set-1 ferdouswahid$ flask run

export FLASK_APP=Task_B.py
python -m flask run
python -m flask run