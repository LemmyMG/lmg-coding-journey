risk_amount = float(input("Enter risk amount: "))
stop_loss = float(input("Enter stop loss pips: "))

dollar_per_pip = risk_amount / stop_loss
lot_size = dollar_per_pip / 10
print ("Risk Amount:", risk_amount)
print ("Stop Loss:", stop_loss)
print ("Dollar per Pip:", "$" + str(dollar_per_pip))
print ("Recommended Lot Size:", lot_size, "lots")
