select category_id, count(*) from products group by category_id;

select supplier_id, avg(price) from products group by supplier_id;

select employee_id, count(*) from orders group by employee_id;

select shipper_id, count(*) from products group by shipper_id;

select city, count(*) from suppliers group by city;

select name, sum(price) from products group by name;

select package_details, count(*) from products group by package_details;

select year(birth_date), count(*) from employees group by year(birth_date);

select order_date, count(*) from orders group by order_date;

select product_id, count(*) from order_details group by product_id;