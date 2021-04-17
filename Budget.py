from Budget import Budget
class Budget:

  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

#deposit method
  def deposit(self, amount):
    old_balance = self.balance
    # this adds the old balance and the amount the user wants to deposit
    self.balance = self.balance + amount

    # this shows the current balance
    return f'old balance: {old_balance}, New balance: {self.balance}'

#withdrawal method
  def withdraw(self, amount):
    old_balance = self.balance
    if(self.balance < amount):
      print('You do not have sufficient funds')
    else:
      self.balance = self.balance - amount
      return f'old balance: {old_balance}, New balance: {self.balance}'

#balance methhod
  def get_balance(self):
    feedback = f'Your budget app balance is {self.balance}'
    return feedback

#transfer method
  def transfer(self, amount, transfer_to):
    if(self.balance < amount):
      print('You do not have suffecient funds')
    else:
      # this subtracts the amount removed from the category transferred from
      self.balance = self.balance - amount
      # this adds the amount transferred to the previous amount in that category
      transfer_to.balance = transfer_to.balance + amount

      feedback = f'You transferred ₦{amount} to {transfer_to.name} \n'
      feedback += f'The balance for {self.name} is now {self.balance} \n'
      feedback += f'The balance for {transfer_to.name} is now {transfer_to.balance}'
      return feedback


# # food_budget is the object from the class, Budget
# foodC = Budget('food', 5000)
# clothingC = Budget('clothing', 2500)
# entertainmentC = Budget('Entertainment', 3500)

# foodC.deposit(1500)

# foodC.withdraw(amount=500)

# foodC.transfer(200, entertainmentC)

# foodC.get_balance()
# clothingC.get_balance()
# entertainmentC.get_balance()

# print(foodC.transfer(100, entertainmentC))
