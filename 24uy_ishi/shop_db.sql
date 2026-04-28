create database shop1_db:

use shop1_db;

create table phones(
    id int auto_increment not null primary key,
    brend varchar(50) not null,
    model varchar(100) not null,
    price decimal(10,2) not null,
    soni int not null,
    ishlab_chiqarilgan_sana datetime not null,
    sreated_at datetime default current_timestamp
);

insert into phones(brend, model, price, soni, ishlab_chiqarilgan_sana) values
('Samsung', 'Galaxy S24', 1000, 15, '2024-01-10 10:00:00'),
('Apple', 'iPhone q5', 1200, 8, '2023-09-20 12:00:00'),
('Xiaomi', 'Redmi 15', 400, 25, '2024-02-05 09:30:00'),
('Samsung', 'Galaxy A55', 600, 20, '2023-11-15 14:00:00'),
('Apple', 'iPhone 14', 900, 5, '2022-09-10 11:00:00');

select brend, model, price, soni from phones;

select brend from phones;

select model, price from phones;

select brend, model, price from phones where price > 1000;

select brend, model, soni from phones where soni < 10;

select brend, model, soni from phones where soni between 15 and 25;

select brend, model, price from phones order by price asc;

select brend, model, soni from phones order by soni desc;

select sum(soni) from phones;

select avg(price) from phones;

select * from phones where year(ishlab_chiqarilgan_sana) = 2024;

select * from phones where year(ishlab_chiqarilgan_sana) > 2022;

select * from phones order by ishlab_chiqarilgan_sana asc limit 1;

select * from phones order by ishlab_chiqarilgan_sana desc limit 1;

select month(ishlab_chiqarilgan_sana) as oy, count(*) as soni from phones group by oy;

select brend, count(*) as telefonlar_soni from phones group by brend;

select brend, avg(price) as ortacha_narx from phones group by brend;

select brend, sum(soni) as telefon_soni from phones group by brend;



