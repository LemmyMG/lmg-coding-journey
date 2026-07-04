package main

import "fmt"

func main() {
	var riskAmount float64
	var stopLossPips float64 

	fmt.Println("Enter risk amount:")
	fmt.Scanln(&riskAmount)

	fmt.Println("Enter stop loss pips:")
	fmt.Scanln(&stopLossPips)

	dollarPerPip := riskAmount / stopLossPips
	lotSize := dollarPerPip / 10
	
		
	fmt.Println("Recommended lotsize =", lotSize,)
}

