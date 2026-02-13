H2 Part1
-- show all customers in Australia
-- show First and Last name of customers in Melbourne
-- show all customers with Credit Limit over $200,000
-- who is the president of the company?
-- how many Sales Reps are in the company?
-- show payments in descending order
-- what was the check# for the payment done on December 17th 2004
-- show product line with the word 'realistic' in the description
-- show product name for vendor 'Unimax Art Galleries'
-- what is the customer number for the highest amount of payment


use classicmodels;
select * from classicmodels.customers
where country = 'Australia'; 

select * from classicmodels.customers

select contactLastName, contactFirstName from classicmodels.customers
where city = 'Melbourne';

select * from classicmodels.customers
where creditLimit >=200.00;

select lastName, firstName from classicmodels.employees
where jobTitle = 'president';

select count(*) from classicmodels.employees
where jobTitle = 'Sales Rep';

select * from  classicmodels.payments
order by amount desc;

select checkNumber from classicmodels.payments
where paymentDate = '2004-12-17';

select productLine from classicmodels.productlines
where textDescription like '%realistic%';

select productName from classicmodels.products
where productVendor = 'Unimax Art Galleries';

select customerNumber from  classicmodels.payments
order by amount desc
limit 1;




