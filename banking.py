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

def process_withdrawal(prompt, balance, min_balance):
    #
    # Write your code here.
    # Define InsufficientFundsError class
    # Define InvalidTransactionError class
    # Validate withdrawal rules
    # Handle all exceptions with appropriate messages
    #
    pass

amount = process_withdrawal("Enter withdrawal amount: $", 1000.00, 100.00)
print(f"Withdrawal successful: ${amount}")
print(f"New balance: ${1000.00 - float(amount)}")
print()

