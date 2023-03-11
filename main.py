import tkinter as tk
from tkinter import messagebox
import csv
import datetime

# Create the main window
root = tk.Tk()
root.title("College Attendance System")

# Define a function to take attendance
def take_attendance():
    # Get the current date
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")

    # Get the name of the class and the total number of students
    class_name = class_entry.get()
    num_students = int(num_entry.get())

    # Create a list to store the attendance data
    attendance = []

    # Loop through each student and record their attendance
    for i in range(1, num_students+1):
        # Get the name of the student
        name = input("Enter the name of student " + str(i) + ": ")
        present = messagebox.askyesno("Attendance", "Is " + name + " present?")
        if present:
            status = "Present"
        else:
            status = "Absent"
        attendance.append([date, class_name, name, status])

    # Save the attendance data to a CSV file
    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(attendance)

    # Display a message box confirming the attendance has been taken
    messagebox.showinfo("Attendance", "Attendance has been taken.")

# Create the labels and entry fields for class name and number of students
class_label = tk.Label(root, text="Class Name:")
class_label.pack()
class_entry = tk.Entry(root)
class_entry.pack()

num_label = tk.Label(root, text="Number of Students:")
num_label.pack()
num_entry = tk.Entry(root)
num_entry.pack()

# Create a button to take attendance
button = tk.Button(root, text="Take Attendance", command=take_attendance)
button.pack()

# Start the main loop
root.mainloop()
