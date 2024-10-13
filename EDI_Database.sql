CREATE DATABASE edi_project;
USE edi_project;

CREATE TABLE login (
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
	contact VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

select*from login;
