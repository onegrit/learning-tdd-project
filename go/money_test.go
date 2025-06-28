package main
import (
	"testing"
)

func assertEqual(t *testing.T, expected Money, actual Money){
	if expected != actual {
		t.Errorf("Expected: [%+v], got: [%+v]", expected, actual)
	}
}

func TestMultiplicationInEuros(t *testing.T){
	tenEuros := Money{
		amount: 10,
		currency: "EUR",
	}
	actualMoneyAfterMultiplication := tenEuros.Times(2)
	exptectedMoneyAfterMultiplication := Money{
		amount: 20,
		currency: "EUR",
	}

	assertEqual(t, exptectedMoneyAfterMultiplication, actualMoneyAfterMultiplication)

}

func TestMultiplicationInDollars(t *testing.T){
	fiver := Money{amount: 5,currency: "USD",}
	actualResult := fiver.Times(2)
	expectedResult := Money{amount: 10, currency: "USD"}

	assertEqual(t, expectedResult, actualResult)
}

func TestDivision(t *testing.T){
	originalMoney := Money{
		amount: 4002,
		currency: "KRW",
	}
	actualMoneyAfterDivision := originalMoney.Divide(4)
	expectedMoneyAfterDivision := Money{amount:1000.5,currency: "KRW"}

	assertEqual(t, expectedMoneyAfterDivision, actualMoneyAfterDivision)

}

type Money struct{
	amount float64 
	currency string
}


// 方法:func (receiver type)methodName(parameter type)(return type)
// func (d Money)Times(multiplier int) Money{
	// return Money{amount:d.amount * multiplier}
// }

func (m Money)Times(multiplier int)Money{
	return Money{
		amount: m.amount * float64(multiplier),
		currency: m.currency,
	}
}

func (m Money)Divide(divisor int)Money{
	return Money{
		amount: m.amount / float64(divisor),
		currency: m.currency,
	}
}