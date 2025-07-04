package stocks

import "errors"

type Bank struct {
	exchangeRates map[string]float64
}

func (b Bank) AddExchangeRate(currencyFrom string, currencyTo string, rate float64) {
	key := currencyFrom + "->" + currencyTo
	b.exchangeRates[key] = rate
}

func (b Bank) Convert(money Money, currencyTo string) (convertedMoney *Money, err error) {
	var result Money
	if money.currency == currencyTo {
		result = NewMoney(money.amount, money.currency)
		return &result, nil
	}

	key := money.currency + "->" + currencyTo
	rate, ok := b.exchangeRates[key]

	if !ok {
		return nil, errors.New(key)
	}

	result = NewMoney(money.amount*rate, currencyTo)
	return &result, nil
}

func NewBank() Bank {
	return Bank{
		exchangeRates: make(map[string]float64),
	}
}
