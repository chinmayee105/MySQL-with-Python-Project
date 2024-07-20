select * from mobile ; 

select distinct Brands from  mobilecompany.mobile; 

select Brands, AVG(Price) as average_price FROM mobile GROUP BY Brands;

select * FROM mobile ORDER BY Price DESC Limit 1 ;

select Brands, COUNT(*) as total_mobile FROM mobile GROUP BY Brands ;

select Brands, AVG(RAM_Storage) as average_RAM FROM mobile GROUP BY Brands 
ORDER BY average_RAM DESC
LIMIT 1 ;

select * FROM mobile WHERE Battery_Capacity > 4000 ;


select Brands, AVG(Price) as average_price FROM mobile
GROUP BY Brands 
ORDER BY average_price ASC
LIMIT 1 ; 


select * FROM mobile WHERE Internal_Storage >= 128 AND RAM_Storage >= 6;


select Brands, AVG(Price) AS average_price, COUNT(*) AS
count FROM mobile
GROUP BY Brands ;

select Brands, AVG(Internal_Storage) AS
average_storage FROM mobile
GROUP BY Brands ;


select price FROM mobile ;