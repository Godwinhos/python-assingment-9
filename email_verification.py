# ===== TASK 2: Email Validator =====
# Create a custom InvalidEmailError exception
# The function should validate email format and raise InvalidEmailError if:
# - Email doesn't contain exactly one '@' symbol
# - Email doesn't contain at least one '.' after the '@'
# If input is empty, raise ValueError with message "Error: email cannot be empty"
# Keep asking until a valid email is entered

print("=== Task 2: Email Validator ===")
print("Email must contain '@' and a domain with '.'\n")
class InvalidEmailError(Exception):
    pass
def validate_email(prompt):
    should_prompt = True
    while should_prompt:
        email = input(prompt).strip()
        try:
            if not email:
                raise InvalidEmailError("Error: email cannot be emptyy")
            if email.count("@") != 1:
                raise InvalidEmailError("email must contain one @ symbol")
            main, domain = email.split("@")
            if "." not in domain:
                raise InvalidEmailError("domain must contain '.'")
            should_prompt = False
        except ValueError as v:
            print(v)
        except InvalidEmailError as z:
            print(z)
        



email = validate_email("Enter your email: ")
print(f"Email accepted: {email}")
print()
