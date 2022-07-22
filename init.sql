
CREATE DATABASE IF NOT EXISTS sales;
USE sales;
CREATE TABLE IF NOT EXISTS units(
    uuid varchar(50) primary key,
    updateTime timestamp not null,
    name varchar(50) not null,
    ntype int not null,
    parentID varchar(50),
    price int
);
CREATE TABLE IF NOT EXISTS history(
    uuid varchar(50) not null references units,
    updateTime timestamp not null,
    price int,
    primary key(uuid, updateTime, price)
);