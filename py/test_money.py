import unittest
import functools
import operator

class Money:
  def __init__(self, amount, currency):
    self.amount = amount
    self.currency = currency
    
  def times(self, multiplier):
    return Money(self.amount * multiplier, self.currency)
  
  def divide(self,divisor):
    return Money(self.amount / divisor, self.currency)
  
  def __eq__(self, other):
    return self.amount == other.amount and self.currency == other.currency

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
    # return Money(total_amount, currency) 

class TestMoney(unittest.TestCase):
  def testMultiplicationInDollars(self):
    fiveDollars = Money(5,"USD")
    tenDollars= Money(10,"USD") 
    self.assertEqual(fiveDollars.times(2),tenDollars)
    # self.assertEqual("USD", tenner.currency)
  
  def testMultiplicationInEuros(self):
    tenEuros = Money(10,"EUR")
    twentyEuros = Money(20,"EUR") 
    self.assertEqual(tenEuros.times(2), twentyEuros)

  def testDivision(self):
    originalMoney = Money(1000.5, "KRW")
    actualMoneyAfterDivision = originalMoney.divide(4)
    expectedMoneyAfterDivision = Money(250.125, "KRW")

    self.assertEqual(expectedMoneyAfterDivision, actualMoneyAfterDivision)
  
  def testAddition(self):
    fiveDollars = Money(5, "USD")
    tenDollars = Money(10, "USD")
    fifteenDollars = Money(15, "USD")
    
    portfolio = Portfolio()
    portfolio.add(fiveDollars, tenDollars)
    
    self.assertEqual(portfolio.evaluate("USD"), fifteenDollars, 'Expected portfolio to contain 5 and 10 dollars')
    
if __name__ == '__main__':
    unittest.main()
