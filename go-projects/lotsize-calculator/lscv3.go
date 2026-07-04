package main

import "fmt"

func calculateLotSize(riskAmount float64, stopLossPips float64) float64 {
	dollarPerPip := riskAmount / stopLossPips
	return dollarPerPip / 10
}

func main() {
	var riskAmount float64
	var stopLossPips float64

	fmt.Print("Enter risk amount ($): ")
	fmt.Scanln(&riskAmount)

	fmt.Print("Enter stop loss (pips): ")
	fmt.Scanln(&stopLossPips)

	lotSize := calculateLotSize(riskAmount, stopLossPips)

	fmt.Println()
	fmt.Println("----- LOT SIZE REPORT -----")
	fmt.Println("Risk Amount:", riskAmount)
	fmt.Println("Stop Loss Pips:", stopLossPips)
	fmt.Println("Recommended Lot Size:", lotSize)

	fmt.Println()
}