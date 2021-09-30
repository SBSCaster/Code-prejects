CREATE TABLE sub_contractors (
id int PRIMARY KEY,
company_name varchar(50),
location varchar(50),
comments varchar(250));

CREATE TABLE insurance (
policy_number varchar(50) PRIMARY KEY,
insurance_company varchar(50),
coverage_type varchar(50));

CREATE TABLE customers(
id int PRIMARY KEY,
name varchar(50),
phone varchar(50),
address varchar(50));

CREATE TABLE services (
id int PRIMARY KEY,
service_type varchar(50),
cost money,
excepted_time varchar(50),
basic_supplies varchar(250));


CREATE TABLE employees (
name varchar(50),
sub_contractor_id int,
CONSTRAINT fkey FOREIGN KEY (sub_contractor_id) REFERENCES sub_contractors(id),
insurance_policy_number varchar(50),
CONSTRAINT fkey2 FOREIGN KEY (insurance_policy_number) REFERENCES insurance(policy_number),
phone_number varchar(50),
deployment_status bool);

CREATE TABLE job_history(
id int PRIMARY KEY,
customer_id int,
CONSTRAINT fkey FOREIGN KEY (customer_id) REFERENCES customers(id),
employee_id int,
CONSTRAINT fkey2 FOREIGN KEY (employee_id) REFERENCES employees(id),
loaction varchar(50),
paid money,
service_id int,
CONSTRAINT fkey3 FOREIGN KEY (service_id) REFERENCES services(id));