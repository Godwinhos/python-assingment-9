# ===== TASK 1: Password Validator =====
# Create a custom WeakPasswordError exception
# The function should validate password strength and raise WeakPasswordError if:
# - Password is less than 8 characters
# - Password doesn't contain at least one digit
# If input is empty, raise ValueError with message "Error: password cannot be empty"
# Keep asking until a valid password is entered

print("=== Task 1: Password Validator ===")
print("Password must be at least 8 characters and contain at least one digit\n")
class WeakpasswordError(Exception):
    pass
def validate_password(prompt):
    should_prompt =True
    while should_prompt:
        password = input(prompt)
        try:
            if not password:
                raise ValueError("error: password cannot be empty")
            if len(password) <8:
                raise WeakpasswordError("error: password must be at least 8 characters")
            if not any(char.isdigit() for char in password):
                raise WeakpasswordError("error: password must contain at least on digit")
            return password
            should_prompt = False
        except ValueError as a:
            print(a)
        except WeakpasswordError as b:
            print(b)


password = validate_password("Enter your password: ")
print(f"Password accepted: {'*' * len(password)}")
print()