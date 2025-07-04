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
    # else:
    #   key = f"{m.currency}->{currency}"
    #   rate = exchangeRates.get(key)
    # if rate is None:
    #   return None
    key = f"{m.currency}->{currency}"
    return m.amount * exchangeRates[key]  
  
  def evaluate(self, currency):
    failures = []
    total = 0.0

    for m in self.moneys:
      try:
        total += self.__convert(m, currency)
      except KeyError as ke:
        failures.append(ke.args[0])

    if len(failures) > 0:
      # failures_str = ','.join(str(f) for f in failures)
      failures_str = ','.join(failures)
      raise Exception(f"Missing exchange rate(s):[{failures_str}]")
      
    return Money(total,currency)