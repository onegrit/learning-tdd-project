import * as assert from 'assert';
import { Money } from './money.mjs';
import { Portfolio } from './portfolio.mjs';
import { Bank } from './bank.mjs'

class MoneyTest {
  constructor() {
    this.bank = new Bank();
    this.bank.addExchangeRate("EUR", "USD", 1.2);
    this.bank.addExchangeRate("USD", "KRW", 1100);
  }
  testMultiplication() {
    let tenEuros = new Money(10, "EUR")
    let twentyEuros = new Money(20, "EUR")
    assert.deepStrictEqual(tenEuros.times(2), twentyEuros, 'Expected 20 euros');
  }

  testDivision() {
    let originalMoney = new Money(4002.0, "KRW");
    let actualMoneyAfterDivision = originalMoney.divide(4);
    let expectedMoneyAfterDivision = new Money(1000.5, "KRW");
    assert.deepStrictEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision,
      `Expected: ${JSON.stringify(expectedMoneyAfterDivision)}, got: ${JSON.stringify(actualMoneyAfterDivision)}`);
  }

  testAddition() {
    let tenEuros = new Money(10, "EUR");
    let twentyEuros = new Money(20, "EUR");
    let thirtyEuros = new Money(30, "EUR");
    let portfolio = new Portfolio();
    portfolio.add(tenEuros, twentyEuros);
    assert.deepStrictEqual(portfolio.evaluate(this.bank, "EUR"), thirtyEuros,
      `Expected: ${JSON.stringify(thirtyEuros)}, got: ${JSON.stringify(portfolio.evaluate(this.bank, "EUR"))}`);
  }

  testAddtionOfDollarsAndWons() {
    const oneDollar = new Money(1, "USD");
    const elevenHundredWon = new Money(1100, "KRW");
    let portfolio = new Portfolio();
    portfolio.add(oneDollar, elevenHundredWon);

    let expectedValue = new Money(2200, "KRW"); // Assuming 1 USD = 1000 KRW for simplicity
    let actualValue = portfolio.evaluate(this.bank, "KRW");

    assert.deepStrictEqual(actualValue, expectedValue,
      `Expected: ${JSON.stringify(expectedValue)}, got: ${JSON.stringify(actualValue, "KRW")}`);
  }


  testAdditionWithMultipleMissingExchangeRates() {
    let oneDollar = new Money(1, "USD");
    let oneEuro = new Money(1, "EUR");
    let oneWon = new Money(1, "KRW");
    let portfolio = new Portfolio();
    portfolio.add(oneDollar, oneEuro, oneWon);

    let expectedError = new Error("Missing exchange rate(s):[USD->Kalgnid,EUR->Kalgnid,KRW->Kalgnid]");

    assert.throws(() => {
      portfolio.evaluate(this.bank, "Kalgnid");
    }, expectedError)

  }

  testConversion() {
    let bank = new Bank();
    bank.addExchangeRate("EUR", "USD", 1.2)
    let tenEuros = new Money(10, "EUR")
    assert.deepStrictEqual(
      bank.convert(tenEuros, "USD"), new Money(12, "USD")
    )
  }

  testConversionWithMissingExchangeRate() {
    let bank = new Bank()
    let tenEuros = new Money(10, "EUR")
    let expectedError = new Error("EUR->Kalgnid");

    assert.throws(() => {
      bank.convert(tenEuros, "Kalgnid")
    }, expectedError)
  }
  getAllTestMethods() {
    let moneyPrototype = MoneyTest.prototype;
    let allProps = Object.getOwnPropertyNames(moneyPrototype);
    let testMethods = allProps.filter(p => {
      return typeof moneyPrototype[p] === 'function' && p.startsWith('test');
    })

    return testMethods;
  }

  runAllTests() {
    let testMethods = this.getAllTestMethods();
    testMethods.forEach(m => {
      console.log(`Running test: ${m}`);
      let method = Reflect.get(this, m);
      try {
        Reflect.apply(method, this, []);
      } catch (e) {
        if (e instanceof assert.AssertionError) {
          console.error(`Test ${m} failed: ${e.message}`);
        }
        else {
          throw e;
        }
      }
    });
  }
}

new MoneyTest().runAllTests();



