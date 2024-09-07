CREATE DATABASE college;
use college;

create table student(
rollno int primary key,
name varchar(50),
marks int not null,
grade varchar(1),
city varchar(50)
);
 insert into student (rollno,name,marks,grade,city)
 values
 (101,"anil",78,"C","pune"),
 (102,"bhumika",93,"A","mumbai"),
 (103,"chetan",85,"B","mumbai"),
 (104,"dhruva",96,"A","delhi"),
 (105,"emanuel",12,"F","delhi"),
 (106,"farah",82,"B","delhi");
 
 select * from student;
 select name,city,marks from student where (marks>90) or city="mumbai";
 select distinct city from student;
 select * from student where marks between 80 and 100;
 select * from student where city in ("delhi","mumbai"); 
 select * from student where city not in ("delhi","mumbai");
 select * from student limit 3;
 select * from student order by grade,city asc;
 select * from student order by marks desc limit 3;
 select max(marks) from student;
 select avg(marks) from student;
 select sum(marks) from student;
 select count(name) from student;
 select city ,avg(marks) from student group by city order by avg(marks) desc;
 

