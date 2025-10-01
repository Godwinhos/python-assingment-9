# ===== TASK 1: Password Validator =====
# Create a custom WeakPasswordError exception
# The function should validate password strength and raise WeakPasswordError if:
# - Password is less than 8 characters
# - Password doesn't contain at least one digit
# If input is empty, raise ValueError with message "Error: password cannot be empty"
# Keep asking until a valid password is entered

print("=== Task 1: Password Validator ===")
print("Password must be at least 8 characters and contain at least one digit\n")

def validate_password(prompt):
    #
    # Write your code here.
    # Define WeakPasswordError class
    # Validate password rules
    # Handle exceptions and keep prompting
    #
    pass

password = validate_password("Enter your password: ")
print(f"Password accepted: {'*' * len(password)}")
print()