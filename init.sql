
CREATE DATABASE IF NOT EXISTS sales;
USE sales;
CREATE TABLE IF NOT EXISTS units(
    uuid varchar(30) primary key,
    updateTime timestamp not null,
    name varchar(50) not null,
    ntype varchar(10) not null,
    parentID varchar(30),
    price int not null,
    children varchar(200)
)