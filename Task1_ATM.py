class ATM:
    def __init__(self,balance=0,pin='1234'):
        self.balance=balance
        self.pin=pin
    
    def authenticate(self):
        input_pin=input("enter your pin:")
        if input_pin==self.pin:
            print("Authentication Successful.")
            return True
        else:
            print("Invalid pin!")
            return False
    
    def change_pin(self):
        current_pin=input("enter your current pin:")
        if current_pin==self.pin:
            new_pin=input("enter your new pin:")
            confirm_pin=input("confirm your pin:")
            if new_pin==confirm_pin:
                self.pin=new_pin
                print("PIN Changed Successfully")
            else:
                print("NEW PIN and Confirmation PIN does not match!")
        else:
            print("Incorrect current pin!")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"${amount} Deposited Successfully.")
        else:
            print("Invalid Deposit Amount")
    
    def withdraw(self,amount):
        if (amount>0 and amount<=self.balance):
            self.balance-=amount
            print(f"${amount} withdrawn successfully")
        else:
            print("Invalid or insufficient Funds")

def main():
    atm=ATM()
    authenticated=False
    while not authenticated:
        authenticated=atm.authenticate()
    
    while True:
        print("\n Welcome to the ATM")
        print("1. Check Balance") 
        print("2. Deposit") 
        print("3. Withdraw") 
        print("4. Change PIN") 
        print("5. Exit")

        choice=input("enter your choice:")
        if choice=='1':
            atm.check_balance()
        elif choice=='2':
            amount=float(input("enter deposit amount:"))
            atm.deposit(amount)
        elif choice=='3':
            amount=float(input("enter deposit amount:"))
            atm.withdraw(amount)
        elif choice=='4':
            atm.change_pin()
        elif choice=='5':
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__=="__main__":
    main()
