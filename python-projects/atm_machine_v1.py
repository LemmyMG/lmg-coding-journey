balance = 1000

while True:
    print("\n=== LMG BANK ===")
    print("1. Check Balance")
    print("2. Exit")
    
    choice = float(input("Choose an option: "))

    if choice == 1:
        print(f"Your current balance is: ${balance}")

    elif choice == 2:
        print("Thank you for using LMG BANK. Goodbye!")
        break