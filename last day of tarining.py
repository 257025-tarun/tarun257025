
-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  Name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert


-- insert
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0001, 'AMAN', 'Sales');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0002, 'SATPREET', 'Accounting');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0003, 'TARUN', 'Sales');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0004, 'VISHAL', 'Accounting');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0005, 'RISHABH', 'Sales');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0006, 'AYUSH', 'Sales');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0007, 'RACHIT', 'Teacher');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0008, 'ROHAN', 'Teacher');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0009, 'ANASH', 'Sales');
INSERT INTO EMPLOYEE (empID, Name, dept) VALUES (0010, 'ANISH', 'Accounting');

-- fetch 
-- SELECT * FROM EMPLOYEE;

-- SELECT * FROM EMPLOYEE where empID > 0002
-- SELECT * FROM EMPLOYEE where dept = 'sales';

-- delete FROM EMPLOYEE where empID = 5;
-- SELECT * FROM EMPLOYEE;

-- SELECT * FROM EMPLOYEE where not empID = 0004 and empID >= 0002 and empID <=0005;
SELECT* FROM EMPLOYEE where not dept = 'Teacher';