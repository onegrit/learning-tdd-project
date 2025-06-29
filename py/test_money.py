import unittest
from money import Money
from portfolio import Portfolio
    # return Money(total_amount, currency) 

class TestMoney(unittest.TestCase):
  def testMultiplication(self):
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
