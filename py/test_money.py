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
    
  def testAdditionOfDollarsAndEuros(self):
    fiveDollars = Money(5, "USD")
    tenEuros = Money(10, "EUR")
    
    portfolio = Portfolio()
    portfolio.add(fiveDollars, tenEuros)
    
    # Assuming the conversion rate is 1 EUR = 1.2 USD
    expectedValue= Money(17, "USD") 
    actualValue = portfolio.evaluate("USD")
    
    self.assertEqual(expectedValue,actualValue, '%s != %s' % (expectedValue, actualValue))
  
  def testAdditionOfDollarsAndWons(self):
    """Test addition of two different currencies: Dollars and Wons"""
    oneDollary = Money(1, "USD")
    elevenHundredWon = Money(1100, "KRW")
    
    portfolio = Portfolio()
    portfolio.add(oneDollary, elevenHundredWon)
    
    # Assuming the conversion rate is 1 USD = 1000 KRW for simplicity
    expectedValue = Money(2200, "KRW") 
    actualValue = portfolio.evaluate("KRW")
    
    self.assertEqual(expectedValue, actualValue, '%s != %s' % (expectedValue, actualValue))
if __name__ == '__main__':
    unittest.main()
