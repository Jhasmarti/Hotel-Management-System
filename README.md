# 🏨 Hotel Management System

## 📌 Overview

The **Hotel Management System** is a **Python + MySQL** based project that provides a command-line interface to manage hotel operations like customer registration, room booking, restaurant orders, laundry services, and total bill generation.

It’s a simple yet functional management system meant for small-scale hotels to automate and manage their business operations effectively.

---

## 🛠 Tech Stack

- **Programming Language**: Python 3
- **Database**: MySQL
- **Libraries Used**:
  - `mysql.connector`
  - `os`
  - `platform`
  - `pandas`
  - `datetime`

---

## 🎯 Features

- ✅ Customer registration with name, address, check-in/check-out date.
- ✅ View available room types.
- ✅ Calculate room rent based on room type and stay duration.
- ✅ View restaurant menu and order food items.
- ✅ Generate restaurant bills based on food and quantity.
- ✅ Laundry billing.
- ✅ Complete bill calculation and printing.

---


---



## 🚀 How to Run
pip install mysql-connector-python pandas
### mydb = con.connect(user='root', password='1234567890', host='localhost', database='hotel')
python hotel_management.py


## 🗃 Database Setup

You’ll need to create a MySQL database named `hotel` with the following tables:

### 1. `custdata`
```sql
CREATE TABLE custdata (
    custname VARCHAR(100),
    addr VARCHAR(255),
    indate DATE,
    outdate DATE
);

CREATE TABLE roomtype (
    room_id INT PRIMARY KEY,
    room_type VARCHAR(50),
    price_per_night INT
);

CREATE TABLE restaurent (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    price INT
);

CREATE TABLE laundary (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    price_per_cloth INT
);
