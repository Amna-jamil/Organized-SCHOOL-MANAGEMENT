import tkinter as tk
from add_student import AddStudentWindow
from update_student import UpdateStudentWindow   # ✅ update student import

def add_student():
    AddStudentWindow(root)

def update_student():
    UpdateStudentWindow(root)   # ✅ ab connect kar diya

def delete_student():
    pass  # will connect later

def view_students():
    pass  # will connect later

def mark_attendance():
    pass  # will connect later

def view_attendance():
    pass  # will connect later

# Main Window
root = tk.Tk()
root.title("School Management System")
root.geometry("400x400")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="School Management System", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

btn1 = tk.Button(root, text="Add Student", width=25, command=add_student)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Update Student", width=25, command=update_student)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Delete Student", width=25, command=delete_student)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="View Students", width=25, command=view_students)
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Mark Attendance", width=25, command=mark_attendance)
btn5.pack(pady=5)

btn6 = tk.Button(root, text="View Attendance", width=25, command=view_attendance)
btn6.pack(pady=5)

root.mainloop()

