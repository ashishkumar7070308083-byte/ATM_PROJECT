import data
import operations

def atm():
    
    while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                operations.check_balance()
            elif choice == 2:
                operations.deposit()
            elif choice == 3:
                operations.withdraw()
            elif choice == 4:
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid choice!")


atm()