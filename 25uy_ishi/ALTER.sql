alter table products add stock int;

alter table employees add email varchar(100);

alter table suppliers modify phone varchar(150);

alter table shippers add country varchar(100);

alter table orders rename column shipper_id to carrier_id;

alter table customers drop column postal_code;

alter table products rename column unit to package_details;

alter table employees drop column photo;

alter table categories add is_active boolean;

alter table suppliers modify country varchar(150) default 'USA';