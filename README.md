# Bank Management System (Python + MySQL)

This is a Bank Management System built using Python and MySQL.

## Features

- Login System
- Create Account
- Deposit Money
- Withdraw Money
- Search Account
- Check Balance
- Display All Accounts
- Delete Account
- Transaction History

## Technologies Used

- Python
- MySQL


## Project Structure

- main.py              # Main program
- bank_operations.py   # All bank functions
- database.py          # Database connection
- database.sql         # Database tables
- requirements.txt     # Project dependencies

### Setup MySQL Database

**Create database and table:**

--- sql
CREATE DATABASE bankdb;

USE bankdb;

CREATE TABLE accounts(
acc_no VARCHAR(20) PRIMARY KEY,
name VARCHAR(50),
balance INT
);

CREATE TABLE transactions(
id INT AUTO_INCREMENT PRIMARY KEY,
acc_no VARCHAR(20),
type VARCHAR(20),
amount INT
);

CREATE TABLE users(
username VARCHAR(20),
password VARCHAR(20)
);
---
-- Default admin login
INSERT INTO users VALUES("admin27","admin@27");


**Run the Project**

- python main.py



**Example Menu**

Bank Management System

- Login System
- Create Account
- Deposit Money
- Withdraw Money
- Search Account
- Check Balance
- Display All Accounts
- Delete Account
- Transaction History
- Exit

**Author**

- **Navneet Singh**

- **Python Developer**

