delete from products where price < 5;

delete from  employees where year(birth_date) > 1970;

delete from shippers where phone = '';

delete from products where unit not like '%kg%'; 

delete from suppliers where country = 'Paris';

delete from products where name like '%sugar%';
