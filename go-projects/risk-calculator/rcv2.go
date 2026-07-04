package main

import "fmt"

func main() {

	 var accountSize float64
	 var riskPercentage float64

	 fmt.Println("Enter account size:")
	 fmt.Scanln(&accountSize)

	 fmt.Println("Enter risk percentage:")
	 fmt.Scanln(&riskPercentage)

	 riskAmount := accountSize * riskPercentage / 100
	 
	 fmt.Println()
	 fmt.Println("------ RISK REPORT ------")
	
	 fmt.Println("Account Size:", accountSize)
	 fmt.Println("Risk Percentage:", riskPercentage)
	 fmt.Println("Your risk Amount is:", riskAmount,"USD")

	  if riskPercentage > 2 {
		fmt.Println("Warning: Risk exceeds 2% of account size.")

	 } else {
		fmt.Println("Acceptable risk level for account size.")
	 }
		fmt.Println()
}