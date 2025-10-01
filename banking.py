# ===== TASK 4: Bank Account Withdrawal System =====
# Create TWO custom exceptions:
# - InsufficientFundsError: raised when withdrawal amount exceeds balance
# - InvalidTransactionError: raised when amount is negative or zero
# 
# The function should:
# - Accept prompt, current balance, and minimum balance (for overdraft protection)
# - Validate withdrawal amount is a valid number (raise ValueError if not)
# - Check if amount is positive (raise InvalidTransactionError if not)
# - Check if withdrawal would bring balance below minimum (raise InsufficientFundsError if so)
# - Return the withdrawal amount if valid
# - Keep asking until valid input

print("=== Task 1: Bank Account Withdrawal System ===")
print("Current Balance: $1000.00")
print("Minimum Balance: $100.00\n")
class InsufficientFundsError(Exception):
    pass
class InvalidTransactionError(Exception):
    pass
def process_withdrawal(prompt, balance, min_balance):
    should_prompt =True
    while should_prompt:
        user_input = input(prompt)
        try:
            amount = float(user_input)
            if amount <= 0:
                raise InvalidTransactionError("error: amount must be positive")
            if balance - amount < min_balance:
                raise InsufficientFundsError("error: insufficient funds for withdrawal")
            return amount
            should_prompt = False
        except ValueError:
            print("error: invalid number format")
        except InvalidTransactionError as inv:
            print(inv)

amount = process_withdrawal("Enter withdrawal amount: $", 1000.00, 100.00)
print(f"Withdrawal successful: ${amount}")
print(f"New balance: ${1000.00 - float(amount)}")
print()

