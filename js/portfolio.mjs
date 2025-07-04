import { Money } from "./money.mjs"; // Use ES6 module import
import { Bank } from './bank.mjs';

export class Portfolio {
  constructor() {
    this.moneys = [];
  }
  add(...moneys) {
    this.moneys = this.moneys.concat(moneys);
  }

  evaluate(bank, currency) {
    let failures = [];
    let total = this.moneys.reduce((sum, money) => {
      try {
        let convertedMoney = bank.convert(money, currency);
        return sum + convertedMoney.amount;
      }
      catch (error) {
        failures.push(`${money.currency}->${currency}`);
        return sum;
      }
    }, 0);

    if (failures.length > 0) {
      throw new Error(`Missing exchange rate(s):[${failures.join()}]`);
    }

    return new Money(total, currency);
  }
}
