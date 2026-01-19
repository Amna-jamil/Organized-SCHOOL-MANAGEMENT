import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="amna17@usman31",
        database="school_management"   # ✅ correct database
    )

def delete_student():
    student_id = entry_id.get().strip()

    if not student_id:
        messagebox.showwarning("Validation", "Please enter Student ID.")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        # ✅ correct column name student_id
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"Student with ID {student_id} deleted successfully.")
        else:
            messagebox.showwarning("Not Found", f"No student found with ID {student_id}.")

        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter GUI
root = tk.Tk()
root.title("Delete Student")

tk.Label(root, text="Enter Student ID to Delete:").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack(pady=5)

btn_delete = tk.Button(root, text="Delete", command=delete_student, bg="red", fg="white")
btn_delete.pack(pady=10)

root.mainloop()

