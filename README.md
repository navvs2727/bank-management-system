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

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bank-management-system.git
```

### 2. Move to project folder

```bash
cd Bank-Management-System
```

### 3. Install required libraries

```bash
pip install mysql-connector-python
```


### 4. Setup MySQL Database

Create database and tables:

```sql
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

INSERT INTO users VALUES("admin27","admin@27");
```

**Default Login**

- Username: admin27
- Password: admin@27

### 5. Run the project

```bash
python main.py
```

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

