
update employees set notes = 'UK-based employee' where year(birth_date) = 2020;

update products set price = price + 5 where price < 20;

update suppliers set phone = concat('+1',phone) where country = 'Canada';

update employees set notes = 'Senior Staff' where year(birth_date) < 1960;

update products set unit = 'Luxury Item' where price > 100;

update products set name = 'Organic Tofu' where name = 'Tofu';

update suppliers set name = upper(name) where country = 'France';

update shippers set name = concat(name, ' - Ltd');

update employees set notes = 'Multilingual' where first_name = 'Michael';

update suppliers set postal_code = lower(postal_code) where country = 'Germany';
