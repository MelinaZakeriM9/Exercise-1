balance= 25000.00

while True:
    print("What do you wish to do?")
    print("1. Transfer\n2. Withdraw \n3.Check balance")
    print("Press x to exit")

    button= input()
    if button =='1':
        t= float(input("Please enter the amount you wish to transfer: "))
        input("Enter destonation card number: ")
        balance -=t
        print("Transfer succesful")

    elif button =='2':
        w= float(input("Please enter the amount you wish to withdraw: "))
        balance -= w
        print("Withdrawal successful")

    elif button =='3':
        print("Your current balance is ", balance)
        
    elif button == 'x' or 'X': break
    else: print("incrrect command")
