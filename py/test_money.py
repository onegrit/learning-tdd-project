import unittest
from money import Money
from portfolio import Portfolio
from bank import Bank

class TestMoney(unittest.TestCase):
  def setUp(self):
    self.bank = Bank()
    self.bank.addExchangeRate("EUR","USD",1.2)
    self.bank.addExchangeRate("USD","KRW",1100)
    
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
    
    self.assertEqual(portfolio.evaluate(self.bank,"USD"), fifteenDollars, 'Expected portfolio to contain 5 and 10 dollars')
    
  def testAdditionOfDollarsAndEuros(self):
    fiveDollars = Money(5, "USD")
    tenEuros = Money(10, "EUR")
    
    portfolio = Portfolio()
    portfolio.add(fiveDollars, tenEuros)
    
    # Assuming the conversion rate is 1 EUR = 1.2 USD
    expectedValue= Money(17, "USD") 
    actualValue = portfolio.evaluate(self.bank,"USD")
    
    self.assertEqual(expectedValue,actualValue, '%s != %s' % (expectedValue, actualValue))
  
  def testAdditionOfDollarsAndWons(self):
    """Test addition of two different currencies: Dollars and Wons"""
    oneDollary = Money(1, "USD")
    elevenHundredWon = Money(1100, "KRW")
    
    portfolio = Portfolio()
    portfolio.add(oneDollary, elevenHundredWon)
    
    # Assuming the conversion rate is 1 USD = 1000 KRW for simplicity
    expectedValue = Money(2200, "KRW") 
    actualValue = portfolio.evaluate(self.bank,"KRW")
    
    self.assertEqual(expectedValue, actualValue, '%s != %s' % (expectedValue, actualValue))
  
  def testAddtionWithMultipleMissingExchangeRates(self):
    """Test addition with multiple missing exchange rates"""
    oneDollar = Money(1, "USD")
    oneEuro = Money(1, "EUR")
    oneWon = Money(1, "KRW")
    
    portfolio = Portfolio()
    portfolio.add(oneDollar, oneEuro, oneWon)
    
    expectedErrorMessage = "Missing exchange rate(s):[USD->kalgnid,EUR->kalgnid,KRW->kalgnid]"
    
    with self.assertRaises(Exception) as context:
      portfolio.evaluate(self.bank,"kalgnid")
    
  def testConversion(self):
    bank= Bank()
    bank.addExchangeRate("EUR","USD",1.2)
    tenEuros = Money(10,"EUR")
    self.assertEqual(bank.convert(tenEuros,"USD"),Money(12,"USD"))

  def testConversionWithMissingExchangeRate(self):
    aBank:Bank = Bank()
    tenEuros = Money(10,"EUR")
    with self.assertRaisesRegex(Exception,"EUR->Kalgnid") as context:
      aBank.convert(tenEuros,"Kalgnid")
    
if __name__ == '__main__':
    unittest.main()
