import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ================== Database Connection ==================
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # apna MySQL username
            password="amna17@usman31",        # apna MySQL password
            database="school_db"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None


# ================== Add Student Window ==================
class AddStudentWindow(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Add Student")
        self.geometry("350x250")

        # Labels + Entry fields
        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Class:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_class = tk.Entry(self)
        self.entry_class.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Contact:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_contact = tk.Entry(self)
        self.entry_contact.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        btn_add = tk.Button(self, text="Add Student", command=self.add_student)
        btn_add.grid(row=4, column=0, padx=10, pady=15)

        btn_clear = tk.Button(self, text="Clear", command=self.clear_form)
        btn_clear.grid(row=4, column=1, padx=10, pady=15)

    # ================== Methods ==================
    def clear_form(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_class.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)

    def add_student(self):
        name = self.entry_name.get().strip()
        age_text = self.entry_age.get().strip()
        clas = self.entry_class.get().strip()
        contact = self.entry_contact.get().strip()

        # Validation
        if not name or not clas:
            messagebox.showwarning("Validation", "Name and Class are required.")
            return

        age = None
        if age_text:
            try:
                age = int(age_text)
            except ValueError:
                messagebox.showwarning("Validation", "Age must be a number.")
                return

        conn = get_connection()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = "INSERT INTO students (name, age, class, contact) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, age, clas, contact))
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully.")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            try:
                cursor.close()
            except:
                pass
            conn.close()


# ================== Run Directly ==================
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()   # Hide main empty window
    AddStudentWindow(root)
    root.mainloop()
