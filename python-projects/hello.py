balance = float(input("Enter account balance: "))

if balance >= 1000:
    print ("Premium Account.")
elif balance >= 500:
    print ("Standard Account.")
else:
    print ("Basic Account.")