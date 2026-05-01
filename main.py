import tkinter as tk
import re

def check_strength():
    password = entry.get()
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search("[0-9]", password):
        strength += 1
    else:
        suggestions.append("Include numbers")

    if re.search("[@#$%^&+=]", password):
        strength += 1
    else:
        suggestions.append("Add special characters")

    if strength <= 2:
        result = "Weak"
        color = "red"
    elif strength <= 4:
        result = "Medium"
        color = "orange"
    else:
        result = "Strong"
        color = "green"

    output_label.config(text=f"Strength: {result}", fg=color)
    suggestion_label.config(text="\n".join(suggestions))


def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_btn.config(text="Hide Password")
    else:
        entry.config(show='*')
        toggle_btn.config(text="Show Password")


# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x320")
root.configure(bg="#f5f5f5")

# Title
title = tk.Label(root, text="Password Strength Checker",
                 font=("Arial", 16, "bold"), bg="#f5f5f5")
title.pack(pady=15)

# Input field
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

# Show/Hide button
toggle_btn = tk.Button(root, text="Show Password", command=toggle_password)
toggle_btn.pack(pady=5)

# Check button
check_btn = tk.Button(root, text="Check Strength",
                      command=check_strength,
                      bg="#4CAF50", fg="white",
                      font=("Arial", 12, "bold"),
                      padx=20, pady=10)
check_btn.pack(pady=20)

# Output label
output_label = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#f5f5f5")
output_label.pack(pady=5)

# Suggestions label
suggestion_label = tk.Label(root, text="", font=("Arial", 10),
                            fg="gray", bg="#f5f5f5")
suggestion_label.pack(pady=5)

root.mainloop()