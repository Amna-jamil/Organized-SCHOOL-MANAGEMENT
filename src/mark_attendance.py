import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import datetime

# MySQL Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # apna MySQL username
        password="amna17@usman31",  # apna MySQL password
        database="school_management"
    )

class MarkAttendanceWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Mark Attendance")
        self.root.geometry("400x250")

        # Student ID
        tk.Label(root, text="Student ID:", font=("Arial", 12)).pack(pady=5)
        self.entry_id = tk.Entry(root, font=("Arial", 12))
        self.entry_id.pack(pady=5)

        # Status Dropdown
        tk.Label(root, text="Status:", font=("Arial", 12)).pack(pady=5)
        self.status_var = tk.StringVar()
        self.status_dropdown = ttk.Combobox(root, textvariable=self.status_var, font=("Arial", 12))
        self.status_dropdown['values'] = ("Present", "Absent")
        self.status_dropdown.pack(pady=5)

        # Date (auto = today)
        self.today = datetime.date.today()

        # Button
        tk.Button(root, text="Mark Attendance", command=self.mark_attendance, bg="green", fg="white", font=("Arial", 12)).pack(pady=15)

    def mark_attendance(self):
        student_id = self.entry_id.get().strip()
        status = self.status_var.get()

        if not student_id.isdigit():
            messagebox.showerror("Error", "Please enter a valid Student ID.")
            return

        if status not in ["Present", "Absent"]:
            messagebox.showerror("Error", "Please select a valid status.")
            return

        conn = connect_db()
        cursor = conn.cursor()

        try:
            query = "INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)"
            cursor.execute(query, (student_id, self.today, status))
            conn.commit()
            messagebox.showinfo("Success", f"Attendance marked for Student ID {student_id} on {self.today}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

# Run Window
if __name__ == "__main__":
    root = tk.Tk()
    app = MarkAttendanceWindow(root)
    root.mainloop()
