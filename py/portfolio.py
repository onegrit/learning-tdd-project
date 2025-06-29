import functools
import operator
from money import Money

class Portfolio:
  def __init__(self):
    self.moneys= []
    
  def add(self, *moneys):
    self.moneys.extend(moneys)
    # for money in moneys:
      # self.money_list.append(money)
      
  def evaluate(self, currency):
    total = functools.reduce(
      operator.add,map(lambda m: m.amount,self.moneys),0
    )
    return Money(total,currency)
    # total_amount = sum(money.amount for money in self.money_list if money.currency == currency)