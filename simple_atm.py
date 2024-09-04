# Initial bank balance
balance = 500 

while True:
    # Display ATM Menu Options
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    # User Input for Menu Selection
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        # Check Balance
        print(f"Your current balance is ${balance}.")
        continue
    
    elif choice == '2':
        # Withdraw Money
        amount = input("Enter the amount to withdraw: $")
        
        if amount.isdigit():
            amount = int(amount)
            
            if amount > balance:
                print("Insufficient funds. Please enter a lesser amount.")
            else:
                balance -= amount
                print(f"${amount} has been withdrawn. Your new balance is ${balance}.")
        else:
            print("Invalid input. Please enter a valid numeric value.")
        
        continue
    
    elif choice == '3':
        # Deposit Money
        amount = input("Enter the amount to deposit: $")
        
        if amount.isdigit():
            amount = int(amount)
            balance += amount
            print(f"${amount} has been deposited. Your new balance is ${balance}.")
        else:
            print("Invalid input. Please enter a valid numeric value.")
        
        continue
    
    elif choice == '4':
        # Exit the program
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        # Invalid Option
        print("Invalid option. Please select a valid choice (1-4).")
        continue
