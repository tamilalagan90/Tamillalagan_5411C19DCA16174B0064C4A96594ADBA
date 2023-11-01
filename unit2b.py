class BankAccount:
  def __init__(self, name, account_number):
      self.name = name
      self.account_number = account_number
      self.balance = 0.0

  def deposit(self, amount):
      self.balance += amount
      print(f"Deposited ${amount}. New balance: ${self.balance}")

  def withdraw(self, amount):
      if self.balance >= amount:
          self.balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self.balance}")
      else:
          print("Insufficient funds!")

  def display_balance(self):
      print(f"Account holder: {self.name}")
      print(f"Account number: {self.account_number}")
      print(f"Current balance: ${self.balance}")

  # Create a BankAccount object
account_holder = input("Enter the account holder's name: ")
account_number = input("Enter the account number: ")
account = BankAccount(account_holder, account_number)

# Prompt the user for input
print("\nWelcome to the banking system!")
while True:
  print("\nPlease select an option:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Display Balance")
  print("4. Exit")

  option = input("Enter your choice (1-4): ")

  if option == '1':
      amount = float(input("Enter the amount to deposit: "))
      account.deposit(amount)
  elif option == '2':
      amount = float(input("Enter the amount to withdraw: "))
      account.withdraw(amount)
  elif option == '3':
      account.display_balance()
  elif option == '4':
      print("Thank you for using the banking system. Goodbye!")
      break
  else:
      print("Invalid option. Please try again."