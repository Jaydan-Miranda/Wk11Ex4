# Initial balance
balance = 1000  

#  loop to keep showing the ATM menu until the user exits
while True:
    # Display ATM options
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Get user input
    choice = input("Choose an option: ")

    # Option 1: Check Balance
    if choice == '1':
        print(f"Your balance is: {balance}\n")

    # Option 2: Deposit
    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful.")
        print(f"New balance is: {balance}\n")

    # Option 3: Withdraw
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds.\n")
        else:
            balance -= amount
            print("Withdrawal successful.")
            print(f"New balance is: {balance}\n")

    # Option 4: Exit the program
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    # Handle invalid menu option
    else:
        print("Please try again.\n")
