import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# MySQL Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # apna MySQL username
        password="amna17@usman31",       # apna MySQL password
        database="school_db"
    )

