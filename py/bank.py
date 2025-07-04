from money import Money

class Bank:
  def __init__(self):
    self.exchangeRates = {}
  
  def addExchangeRate(self,currencyFrom:str, currencyTo:str,rate:float):
    key = currencyFrom + "->" + currencyTo 
    self.exchangeRates[key]=rate

  def convert(self,aMoney:Money,currency:str)->Money | Exception:
    if aMoney.currency == currency:
      return Money(aMoney.amount,currency)

    key:str = aMoney.currency + "->" + currency
    
    if key in self.exchangeRates:
      return Money(aMoney.amount*self.exchangeRates[key],currency)
    
    raise Exception(key)
      
  
  
