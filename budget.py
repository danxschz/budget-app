# Budget App -- Scientific Computing with Python Project #3

## Main object
class Category:

  # Functions
  def __init__(self, category):
    self.category = category
    self.balance = 0
    self.ledger = list()

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount) is True:
      amount *= -1
      self.ledger.append({"amount": amount, "description": description})
      self.balance += amount
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def transfer(self, amount, category):
    if self.check_funds(amount) is True:
      amount *= -1
      self.ledger.append({"amount": amount, "description": f"Transfer to {category.category}"})
      self.balance += amount
      category.ledger.append({"amount": amount*(-1), "description": f"Transfer from {self.category}"})
      category.balance += amount*(-1)
      return True
    else:
      return False

  def __str__(self):
      header = self.category.center(30, "*") + "\n"
      operationstr = ""
      for item in self.ledger:
        operation = item["description"][:23].ljust(23) + format(item["amount"], ".2f")[:7].rjust(7)
        operationstr += operation + "\n"
      footer = f"Total: {str(round(self.balance,2))[:7]}"
      fullstr = header + operationstr + footer
      return fullstr

## Spend chart
def create_spend_chart(categories):
  spendlist = list()
  for category in categories:
    categorytotal = 0
    for item in category.ledger:
      if item["amount"] < 0:
        amount = item["amount"]
        categorytotal += amount
    spendlist.append(categorytotal)
  total = sum(spendlist)

  percentagelist = list()
  for i in range(len(categories)):
    percentage = (spendlist[i]/total) * 100
    percentagelist.append(percentage)

  # Create chart in descending order by steps of -10
  n = 100
  chart = "Percentage spent by category\n"
  while n >= 0:
    line = str(n).rjust(3) + ("| ")
    for percentage in percentagelist:
      if percentage >= n:
        line += "o  "
      else:
        line += "   "
    chart += line + "\n"
    n -= 10

  namelenghts = list()
  for category in categories:
    namelenght = len(category.category)
    namelenghts.append(namelenght)

  # Create vertical names of categories
  footer = "    -" + (len(categories)*"---") + "\n"
  n = 0
  while n <= (max(namelenghts)-1):
    line = "     "
    for category in categories:
      try:
        character = category.category[n]
      except:
        character = " "
      line += character + "  "
    if n == (max(namelenghts)-1):
      footer += line
    else:
      footer += line + "\n"
    n += 1

  fullchart = chart + footer
  return fullchart
