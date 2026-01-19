School Management System
Project Overview

The School Management System is a desktop-based application developed using Python to manage fundamental school operations in an organized and efficient manner. The system provides a graphical user interface (GUI) built with Tkinter and uses a MySQL database for secure data storage. The project focuses on record management and attendance handling without incorporating machine learning techniques.

Objectives

To automate basic student record management

To reduce manual record keeping

To provide a user-friendly desktop interface

To ensure structured and secure data handling

Features

Add new student records

Update existing student information

Delete student records

View all registered students

Mark student attendance

View attendance history

Technologies Used

Programming Language: Python

GUI Framework: Tkinter

Database: MySQL

Database Connector: mysql-connector-python

Project Structure
School_Management_System/
│
├── menu.py
├── add_student.py
├── update_student.py
├── delete_student.py
├── view_records.py
├── mark_attendance.py
├── db_connect.py
└── README.md

System Requirements

Python 3.x

MySQL Server

MySQL Connector for Python

Install the required package using:

pip install mysql-connector-python

How to Run the Application

Create a MySQL database named school_management.

Create the required tables for students and attendance.

Configure database credentials in db_connect.py.

Execute the main file:

python menu.py

Scope

This project is developed for academic purposes to demonstrate GUI-based application development, database connectivity, and CRUD operations using Python. It does not include machine learning or advanced analytics.

Developer

Amna
BS Artificial Intelligence
