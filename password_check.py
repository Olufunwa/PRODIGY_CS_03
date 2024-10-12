import tkinter as tk
from tkinter import messagebox
import re

# Function to assess password strength
def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    if strength_score == 5:
        return "Strong Password"
    elif strength_score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"

# Function to handle password input and feedback
def check_password():
    password = entry.get()
    feedback = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Password strength: {feedback}")

# Setting up the GUI window
root = tk.Tk()
root.title("Password Strength Checker")

# Adding label and entry box for password input
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

# Entry box to show what you're typing
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Adding button to trigger password strength check
button = tk.Button(root, text="Check Strength", command=check_password)
button.pack(pady=10)

# Run the application
root.mainloop()
