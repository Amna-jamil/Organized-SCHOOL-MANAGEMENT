import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Function to connect database
def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="amna17@usman31",  # apna password daalo
        database="school_management"      # apna DB name daalo
    )

# Tkinter Attendance Viewer
def view_attendance_tk():
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance")
        records = cursor.fetchall()

        # New window for attendance
        win = tk.Toplevel()
        win.title("Attendance Records")
        win.geometry("600x400")

        # Treeview for table
        cols = [desc[0] for desc in cursor.description]  # column names
        tree = ttk.Treeview(win, columns=cols, show="headings")
        tree.pack(fill="both", expand=True)

        # Add headings
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")

        # Insert rows
        for row in records:
            tree.insert("", "end", values=row)

        conn.close()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Example Tkinter Main Window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("School Management System")
    root.geometry("300x200")

    btn = tk.Button(root, text="View Attendance", command=view_attendance_tk)
    btn.pack(pady=20)

    root.mainloop()


