import re

def check_password_strength(password):
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
        return "Weak", suggestions
    elif strength <= 4:
        return "Medium", suggestions
    else:
        return "Strong", suggestions