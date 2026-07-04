package main

import "fmt"

func main() {

var accountSize float64
var riskPercentage float64

fmt.Println("Enter your account size:")
fmt.Scanln(&accountSize)

fmt.Println("Enter risk percentage")
fmt.Scanln(&riskPercentage)

riskAmount := accountSize * riskPercentage / 100

fmt.Println("Account Size:", accountSize)
fmt.Println("Risk Percentage:", riskPercentage)
fmt.Println("Your risk amount is:", riskAmount)

}