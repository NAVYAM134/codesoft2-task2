import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        # Get the password length from the entry field
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be positive!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a number.")
        return

    # Define the character set for the password
    char_set = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    # Display the password in the GUI
    result_label.config(text=f"Generated Password: {password}")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter password length:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Create an entry widget for password length
length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_button.pack(pady=10)

# Create a label to display the generated password
result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

# Run the application
root.mainloop()
