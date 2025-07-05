package main

import (
	"reflect"
	s "tdd/stocks"
	"testing"
)

var bank s.Bank

func init() {
	bank = s.NewBank()
	bank.AddExchangeRate("EUR", "USD", 1.2)
	bank.AddExchangeRate("USD", "KRW", 1100)
}

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

	fiveDollars := s.NewMoney(5, "USD")
	tenDollars := s.NewMoney(10, "USD")
	fifteenDollars := s.NewMoney(15, "USD")

	portfolio = portfolio.Add(fiveDollars)
	portfolio = portfolio.Add(tenDollars)
	portfolioInDollars, err := portfolio.Evaluate(bank, "USD")
	assertNil(t, err)

	assertEqual(t, fifteenDollars, *portfolioInDollars)
}

func TestAddtionOfDollarsAndEuros(t *testing.T) {
	var portfolio s.Portfolio

	fiveDollars := s.NewMoney(5, "USD")
	tenEuros := s.NewMoney(10, "EUR")

	portfolio = portfolio.Add(fiveDollars)
	portfolio = portfolio.Add(tenEuros)
	expectedValue := s.NewMoney(17, "USD") // Assuming 1 EUR = 1.2 USD for simplicity
	actualValue, err := portfolio.Evaluate(bank, "USD")

	assertNil(t, err)
	assertEqual(t, expectedValue, *actualValue)
}

func TestAddtionOfDollarsAndWons(t *testing.T) {
	//两个不同币种相加测试: 1USD + 1100KRW = 2200KRW

	var portfolio s.Portfolio

	oneDollary := s.NewMoney(1, "USD")
	elevenHundredWon := s.NewMoney(1100, "KRW")

	portfolio = portfolio.Add(oneDollary)
	portfolio = portfolio.Add(elevenHundredWon)

	expectedValue := s.NewMoney(2200, "KRW") // Assuming 1 USD = 1000 KRW for simplicity
	actualValue, err := portfolio.Evaluate(bank, "KRW")

	assertNil(t, err)
	assertEqual(t, expectedValue, *actualValue)
}

func TestAdditonWihMultipleMissingExchangeRates(t *testing.T) {
	var portfolio s.Portfolio

	oneDollar := s.NewMoney(1, "USD")
	onEuro := s.NewMoney(1, "EUR")
	oneWon := s.NewMoney(1, "KRW")

	portfolio = portfolio.Add(oneDollar)
	portfolio = portfolio.Add(onEuro)
	portfolio = portfolio.Add(oneWon)

	expectedErrorMessage := "Missing exchange rate(s):[USD->Kalgnid,EUR->Kalgnid,KRW->Kalgnid,]"
	value, actualError := portfolio.Evaluate(bank, "Kalgnid")

	assertNil(t, value)
	assertEqual(t, expectedErrorMessage, actualError.Error())
}

func TestConversionWithDifferenctRatesBetweenTwoCurrencies(t *testing.T) {
	bank := s.NewBank()
	bank.AddExchangeRate("EUR", "USD", 1.2)
	tenEuros := s.NewMoney(10, "EUR")
	actualConvertedMoney, err := bank.Convert(tenEuros, "USD")
	assertNil(t, err)
	assertEqual(t, s.NewMoney(12, "USD"), *actualConvertedMoney)
	bank.AddExchangeRate("EUR", "USD", 1.3)
	actualConvertedMoney, err = bank.Convert(tenEuros, "USD")
	assertNil(t, err)
	assertEqual(t, s.NewMoney(13, "USD"), *actualConvertedMoney)

}

func assertNil(t *testing.T, actual interface{}) {
	if actual != nil && !reflect.ValueOf(actual).IsNil() {
		t.Errorf("Expected to be nil, got: [%+v]", actual)
	}
}

func TestConversionWithMissingExchangeRate(t *testing.T) {
	bank := s.NewBank()
	tenEuros := s.NewMoney(10, "EUR")
	actualConvertedMoney, err := bank.Convert(tenEuros, "Kalgnid")

	if actualConvertedMoney != nil {
		t.Errorf("Expected converted money to be nil, got: [%+v]", actualConvertedMoney)
	}
	assertEqual(t, "EUR->Kalgnid", err.Error())

}
