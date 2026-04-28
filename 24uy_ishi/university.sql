create database university_db;

use university_db;

create table students(
    id int auto_increment primary key,
    name varchar(50) not null,
    fakultet varchar(50) not null,
    kurs int not null,
    yosh int not null,
    qabul_sana datetime not null
);

insert into students (name, fakultet, kurs, yosh, qabul_sana) values
('Anvar',    'Informatika',   1, 18, '2024-09-01 09:00:00'),
('Dilshod',  'Matematika',    2, 19, '2023-09-01 09:00:00'),
('Malika',   'Informatika',   3, 20, '2022-09-01 09:00:00'),
('Shaxnoza', 'Fizika',        1, 18, '2024-09-01 09:00:00'),
('Javohir',  'Matematika',    4, 22, '2021-09-01 09:00:00');

select name, fakultet, kurs, yosh from students;

select name from students;

select fakultet, kurs from students;

select name, yosh from students where yosh > 20;

select name, kurs from students where kurs = 1;

select name, fakultet from students where fakultet = 'Matematika';

select name, yosh from students order by yosh asc;

select name, kurs from students order by kurs desc;

select count(*) from students;

select avg(yosh) from students;

select fakultet, avg(yosh) from students group by fakultet;

select fakultet, min(yosh) from students group by fakultet;

select kurs, count(*) from students group by kurs;

select name, qabul_sana from students where year(qabul_sana) = 2024;

select name, qabul_sana from students where year(qabul_sana) = 2021;

select name, qabul_sana from students order by qabul_sana desc limit 1;

select name, qabul_sana from students order by qabul_sana desc; 

