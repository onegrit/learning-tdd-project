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
    let rate = exchangeRates.get(key);
    if (!rate) {
      return undefined;
    }
    return money.amount * rate;
  }

  evaluate(currency) {
    let failures = [];
    let total = this.moneys.reduce((sum, money) => {
      let convertedAmount = this.convert(money, currency);
      if (convertedAmount === undefined) {
        failures.push(`${money.currency}->${currency}`);
        return sum;
      }
      return sum + convertedAmount;
    }, 0);

    if (failures.length > 0) {
      throw new Error(`Missing exchange rate(s):[${failures.join()}]`);
    }
    return new Money(total, currency);
  }
}
