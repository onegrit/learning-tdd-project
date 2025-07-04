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
  
  def __convert(self,m, currency):
    exchangeRates = {
      "EUR->USD": 1.2,  # Conversion rate from EUR to USD
      "USD->KRW": 1100, # Conversion rate from USD to KRW
    }

    if m.currency == currency:
      return m.amount
    else:
      key = f"{m.currency}->{currency}"
      return m.amount * exchangeRates[key]  
  
  def evaluate(self, currency):
    total = functools.reduce(
      operator.add,map(lambda m: self.__convert(m,currency),self.moneys),0)
    
    return Money(total,currency)
    # total_amount = sum(money.amount for money in self.money_list if money.currency == currency)