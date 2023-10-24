class BankAccount:
  def __init__(self, account_holder, initial_balance=0):
      self.balance = initial_balance
      self.holder = account_holder

  def deposit(self, amount):
      if amount > 0:
          self.balance += amount
          print(f"Deposited ${amount}. New balance: ${self.balance}")
      else:
          print("Invalid deposit amount.")

  def withdraw(self, amount):
      if 0 < amount <= self.balance:
          self.balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self.balance}")
      else:
          print("Invalid withdrawal amount or insufficient funds.")
my_account = BankAccount("John Doe", 1000)

my_account.deposit(500)
my_account.withdraw(200)
  
  
  