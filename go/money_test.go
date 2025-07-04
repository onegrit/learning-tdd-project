package main

import (
	s "tdd/stocks"
	"testing"
)

func assertEqual(t *testing.T, expected interface{}, actual interface{}) {
	if expected != actual {
		t.Errorf("Expected: [%+v], got: [%+v]", expected, actual)
	}
}

func TestMultiplication(t *testing.T) {
	tenEuros := s.NewMoney(10, "EUR")
	actualMoneyAfterMultiplication := tenEuros.Times(2)
	exptectedMoneyAfterMultiplication := s.NewMoney(20, "EUR")

	assertEqual(t, exptectedMoneyAfterMultiplication, actualMoneyAfterMultiplication)

}

func TestDivision(t *testing.T) {
	originalMoney := s.NewMoney(4002, "KRW")
	actualMoneyAfterDivision := originalMoney.Divide(4)
	expectedMoneyAfterDivision := s.NewMoney(1000.5, "KRW")

	assertEqual(t, expectedMoneyAfterDivision, actualMoneyAfterDivision)
}

func TestAddition(t *testing.T) {
	var portfolio s.Portfolio
	var portfolioInDollars s.Money

	fiveDollars := s.NewMoney(5, "USD")
	tenDollars := s.NewMoney(10, "USD")
	fifteenDollars := s.NewMoney(15, "USD")
	portfolio = portfolio.Add(fiveDollars)
	portfolio = portfolio.Add(tenDollars)
	portfolioInDollars, _ = portfolio.Evaluate("USD")

	assertEqual(t, fifteenDollars, portfolioInDollars)
}

func TestAddtionOfDollarsAndEuros(t *testing.T) {
	var portfolio s.Portfolio

	fiveDollars := s.NewMoney(5, "USD")
	tenEuros := s.NewMoney(10, "EUR")

	portfolio = portfolio.Add(fiveDollars)
	portfolio = portfolio.Add(tenEuros)
	expectedValue := s.NewMoney(17, "USD") // Assuming 1 EUR = 1.2 USD for simplicity
	actualValue, _ := portfolio.Evaluate("USD")

	assertEqual(t, expectedValue, actualValue)
}

func TestAddtionOfDollarsAndWons(t *testing.T) {
	//两个不同币种相加测试: 1USD + 1100KRW = 2200KRW

	var portfolio s.Portfolio

	oneDollary := s.NewMoney(1, "USD")
	elevenHundredWon := s.NewMoney(1100, "KRW")

	portfolio = portfolio.Add(oneDollary)
	portfolio = portfolio.Add(elevenHundredWon)

	expectedValue := s.NewMoney(2200, "KRW") // Assuming 1 USD = 1000 KRW for simplicity
	actualValue, _ := portfolio.Evaluate("KRW")

	assertEqual(t, expectedValue, actualValue)
}

func TestAdditonWihMultipleMissingExchangeRates(t *testing.T) {
	var portfolio s.Portfolio

	oneDollar := s.NewMoney(1, "USD")
	onEuro := s.NewMoney(1, "EUR")
	oneWon := s.NewMoney(1, "KRW")

	portfolio = portfolio.Add(oneDollar)
	portfolio = portfolio.Add(onEuro)
	portfolio = portfolio.Add(oneWon)

	expectedErrorMessage := "Missing exchange rate(s):[USD->kalgnid,EUR->kalgnid,KRW->kalgnid,]"
	_, actualError := portfolio.Evaluate("kalgnid")

	// if expectedErrorMessage != actualError.Error() {
	// t.Errorf("Expected : [%s], got: [%s]", expectedErrorMessage, actualError.Error())
	// }
	assertEqual(t, expectedErrorMessage, actualError.Error())
}
