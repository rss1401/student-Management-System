import tkinter as tk
from tkinter import messagebox

class StudentManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management System")
        self.background_image = tk.PhotoImage(file=r"C:\Users\KBPIT\Desktop\jbdhsb\student management.png")  # Replace with the path to your image
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.students = {}

        self.label_id = tk.Label(master, text="Student ID:")
        self.label_name = tk.Label(master, text="Student Name:")
        self.label_grade = tk.Label(master, text="Student Grade:")

        self.entry_id = tk.Entry(master)
        self.entry_name = tk.Entry(master)
        self.entry_grade = tk.Entry(master)

        self.button_add = tk.Button(master, text="Add Student", command=self.add_student)
        self.button_remove = tk.Button(master, text="Remove Student", command=self.remove_student)
       
        self.button_update = tk.Button(master, text="Update Grade", command=self.update_grade)

        self.text_display = tk.Text(master, height=25, width=200)
        
        # Layout
        self.label_id.grid(row=0, column=0)
        self.label_name.grid(row=1, column=0)
        self.label_grade.grid(row=2, column=0)

        self.entry_id.grid(row=0, column=1)
        self.entry_name.grid(row=1, column=1)
        self.entry_grade.grid(row=2, column=1)

        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_remove.grid(row=4, column=0, columnspan=2, pady=10)
      
        self.button_update.grid(row=6, column=0, columnspan=2, pady=10)

        self.text_display.grid(row=7, column=0, columnspan=2, pady=10)


    def add_student(self):
        student_id = self.entry_id.get()
        name = self.entry_name.get()
        grade = self.entry_grade.get()

        if student_id and name and grade:
            self.students[student_id] = {'name': name, 'grade': grade}
            messagebox.showinfo("Success", f"Student {name} added successfully.")
            self.clear_entries()
            self.display_students()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
            
    
    def remove_student(self):
        student_id = self.entry_id.get()

        if student_id in self.students:
            del self.students[student_id]
            messagebox.showinfo("Success", "Student removed successfully.")
            self.clear_entries()
            self.display_students()
        else:
            messagebox.showerror("Error", "Student not found.")
            
    
    def display_students(self):
        self.text_display.delete(1.0, tk.END)  # Clear existing text
        student_list = "\n".join([f"ID: {id}, Name: {details['name']}, Grade: {details['grade']}" for id, details in self.students.items()])
        self.text_display.insert(tk.END, student_list)
        

    def update_grade(self):
        student_id = self.entry_id.get()
        new_grade = self.entry_grade.get()

        if student_id in self.students:
            self.students[student_id]['grade'] = new_grade
            messagebox.showinfo("Success", "Grade updated successfully.")
            self.clear_entries()
            self.display_students()
        else:
            messagebox.showerror("Error", "Student not found.")
    

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_grade.delete(0, tk.END)
        
def main():
    root = tk.Tk()
    sms = StudentManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
