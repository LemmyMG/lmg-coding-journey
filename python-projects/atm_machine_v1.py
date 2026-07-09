balance = 1000

while True:
    print("\n=== LMG BANK ===")
    print("\n1. Check Balance")
    print("2. Exit")
    
    choice = float(input("\nChoose an option: "))

    if choice == 1:
        print(f"Your current balance is: ${balance}")

    elif choice == 2:
        print("Thank you for using LMG BANK. Goodbye!")
