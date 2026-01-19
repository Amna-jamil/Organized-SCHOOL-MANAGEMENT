# update_student.py
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# DB Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="amna17@usman31",
        database="school_management"
    )

class UpdateStudentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Update Student")
        self.root.geometry("400x350")

        # Student ID
        tk.Label(root, text="Student ID").pack(pady=5)
        self.id_entry = tk.Entry(root)
        self.id_entry.pack(pady=5)

        # Fetch button
        tk.Button(root, text="Fetch Student", command=self.fetch_student).pack(pady=5)

        # Student Details
        tk.Label(root, text="Name").pack(pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Age").pack(pady=5)
        self.age_entry = tk.Entry(root)
        self.age_entry.pack(pady=5)

        tk.Label(root, text="Class").pack(pady=5)
        self.class_entry = tk.Entry(root)
        self.class_entry.pack(pady=5)

        tk.Label(root, text="Contact").pack(pady=5)
        self.contact_entry = tk.Entry(root)
        self.contact_entry.pack(pady=5)

        # Update button
        tk.Button(root, text="Update Student", command=self.update_student).pack(pady=10)

    def fetch_student(self):
        student_id = self.id_entry.get()
        if not student_id:
            messagebox.showwarning("Input Error", "Please enter Student ID")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name, age, class, contact FROM students WHERE student_id=%s", (student_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.class_entry.delete(0, tk.END)
            self.contact_entry.delete(0, tk.END)

            self.name_entry.insert(0, result[0])
            self.age_entry.insert(0, result[1] if result[1] else "")
            self.class_entry.insert(0, result[2])
            self.contact_entry.insert(0, result[3] if result[3] else "")
        else:
            messagebox.showerror("Error", "Student not found")

    def update_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        student_class = self.class_entry.get()
        contact = self.contact_entry.get()

        if not student_id or not name or not student_class:
            messagebox.showwarning("Input Error", "Student ID, Name and Class are required")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "UPDATE students SET name=%s, age=%s, class=%s, contact=%s WHERE student_id=%s"
            cursor.execute(query, (name, age if age else None, student_class, contact, student_id))
            conn.commit()
            conn.close()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Student updated successfully")
            else:
                messagebox.showwarning("Error", "No student updated. Check Student ID.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateStudentWindow(root)
    root.mainloop()

