import mysql.connector as sql

myCon = sql.connect(host="localhost", user="root", password="root")
cursor = myCon.cursor()

print("Creating Database and Tables")
database_create = "CREATE DATABASE IF NOT EXISTS library"

cursor.execute(database_create)
myCon.commit()

database_connect = "USE library"

cursor.execute(database_connect)
myCon.commit()

create_books = """CREATE TABLE IF NOT EXISTS books (
                    book_id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    author VARCHAR(255) NOT NULL,
                    isbn VARCHAR(13) NOT NULL,
                    publisher VARCHAR(255) NOT NULL,
                    year YEAR NOT NULL,
                    genre VARCHAR(100) NOT NULL,
                    quantity INT NOT NULL,
                    borrowed_count INT NOT NULL,
                    status CHAR(10) NOT NULL
                );"""

create_members = """CREATE TABLE IF NOT EXISTS  members (
                    member_id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    address VARCHAR(255),
                    phone_number VARCHAR(15) UNIQUE NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    join_date DATE NOT NULL,
                    membership_type ENUM('standard', 'premium', 'student') NOT NULL,
                    status char(10) NOT NULL DEFAULT 'active'
                );"""

create_loans = """CREATE TABLE IF NOT EXISTS loans (
                    loan_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    member_id INT NOT NULL,
                    book_id INT NOT NULL,
                    loan_date DATE NOT NULL,
                    due_date DATE NOT NULL,
                    return_date DATE NULL,
                    status CHAR(10) NOT NULL DEFAULT 'loaned'
                );"""
print("Creating Books Table")
cursor.execute(create_books)
myCon.commit()
print("Creating Members Table")
cursor.execute(create_members)
myCon.commit()
print("Creating Loans Table")
cursor.execute(create_loans)
myCon.commit()
