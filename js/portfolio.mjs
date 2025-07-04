import { Money } from "./money.mjs"; // Use ES6 module import

export class Portfolio {
  constructor() {
    this.moneys = [];
  }
  add(...moneys) {
    this.moneys = this.moneys.concat(moneys);
  }

  convert(money, currency) {
    if (money.currency === currency) {
      return money.amount;
    }

    let exchangeRates = new Map();
    exchangeRates.set("EUR->USD", 1.2);
    exchangeRates.set("USD->KRW", 1100);

    const key = `${money.currency}->${currency}`;
    return money.amount * exchangeRates.get(key);
  }

  evaluate(currency) {
    let total = this.moneys.reduce((sum, money) => {
      return sum + this.convert(money, currency);
    }, 0);
    return new Money(total, currency);
  }
}
