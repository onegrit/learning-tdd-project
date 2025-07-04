import * as assert from 'assert';
import { Money } from './money.mjs';
import { Portfolio } from './portfolio.mjs';

class MoneyTest {
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
    assert.deepStrictEqual(portfolio.evaluate("EUR"), thirtyEuros,
      `Expected: ${JSON.stringify(thirtyEuros)}, got: ${JSON.stringify(portfolio.evaluate("EUR"))}`);
  }

  testAddtionOfDollarsAndWons() {
    const oneDollar = new Money(1, "USD");
    const elevenHundredWon = new Money(1100, "KRW");
    let portfolio = new Portfolio();
    portfolio.add(oneDollar, elevenHundredWon);

    let expectedValue = new Money(2200, "KRW"); // Assuming 1 USD = 1000 KRW for simplicity
    assert.deepStrictEqual(portfolio.evaluate("KRW"), expectedValue,
      `Expected: ${JSON.stringify(expectedValue)}, got: ${JSON.stringify(portfolio.evaluate("KRW"))}`);
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



