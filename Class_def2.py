from os import system, name
import time

Account_list = []                                                               
Acc_Dict = {}                                                                   #Dictionary of Account Number and List Indices

def clear():                                                                    #Clear Console function
    if name == 'nt': 
        _ = system('clear')  
    else: 
        _ = system('clear') 

class Account:
    def __init__(self):                                                         #Account Variables
        self.acc_num  = '\0'
        self.name = '\0'
        self.acc_balance = 0
        self.acc_type = '\0'

    def create_account(self):
        self.choose_account_num()
        self.change_name()
        self.set_acc_type()
        self.deposit()

    def modify_account(self):
        self.change_name()
        self.set_acc_type()

    def change_name(self):
        self.name = input("Enter your name: ")
        if self.name == '':
            print("Please choose a valid name!")
            self.change_name()

    def choose_account_num(self):
        self.acc_num = input("Choose your 4 digit Account number: ")
        if not self.acc_num in Acc_Dict:
            if ((not len(self.acc_num) == 4) or (not self.acc_num.isdigit())):
                print("Please choose a valide Account number!!")
                self.choose_account_num()
            Acc_Dict[self.acc_num] = len(Account_list)-1                        #For every Account Number created, its list index is stored in Dict
        else:
            print("Account Numer Already Exist!! ")
            self.choose_account_num()

    def set_acc_type(self):
        self.acc_type = input("Choose Account type Savings or Current: ")
        if not (self.acc_type=="Savings" or self.acc_type=="Current"):
            print("Invalid Account Type!")
            self.set_acc_type()

    def deposit(self):
        amount = (input("Add balance: "))
        if amount.isdigit():
            amount = int(amount)
            if (amount < 1):
                print("Invalid Ammount")
                self.deposit()
            else:
                self.acc_balance = int(self.acc_balance) + amount
        else:
            print("Invalid Amount!")
            self.deposit()
    
    def withdraw(self):
        amount = (input("Withdraw Amount: "))
        if amount.isdigit():
            amount = int(amount)
            if (amount < 1):
                print("Invalid Ammount")
                self.withdraw()
            elif amount>int(self.acc_balance):
                print("Amount exceeds Current Balance!!")
                self.withdraw()
            else:
                self.acc_balance = int(self.acc_balance) - amount
        else:
            print("Invalid Amount!!")
            self.deposit()

    def return_acc_num(self):
        print("Account Number: ", self.acc_num)

    def return_balance(self):
        print("Account Balance: ", self.acc_balance)

    def return_type(self):
        print("Account Balance: ", self.acc_type)

    def show_account(self):
        print("Account Number: ", self.acc_num)
        print("Your Name is: ", self.name)
        print("Account type: ", self.acc_type)
        print("Account Balance:", self.acc_balance)

def new_account():
    Account_list.append(len(Account_list))
    Account_list[-1] = Account()
    Account_list[-1].create_account()

def working_Account():
    working_acc = input("Enter Account Number  ")
    if not working_acc in Acc_Dict:
        print("Account Does not exist!!")
        working_acc = working_Account()
    else:
        working_acc_num = int(Acc_Dict[working_acc])
        return working_acc_num  
    return working_acc

def Data_tb_form():
    if len(Account_list) == 0:
        print("No Account created")
        pass
    else:
        print("".center(81,'-'))
        print('| {0:14s} | {1:21s} | {2:15s} | {3:18s} |'.format('Account Number', \
            'User Name', 'Account Type', 'Balance'))
        for i in range(0, len(Account_list)):
            print('| {0:14s} | {1:21s} | {2:15s} | Rs {3:14s}  |'.\
                format((Account_list[i].acc_num), Account_list[i].name, \
                    Account_list[i].acc_type, str(Account_list[i].acc_balance)))
        print("".center(81,'-'))
        print("\n")

def Continue_1():
    if  (input("Press 0 to continue ")) == '0':
            clear()
    else:
        Continue_1()


#            !!Command Line Interface!!
clear()
while True:
    print()
    print ("Welcome To Bank".center(81, '-'))
    print()
    print("How Can We Help You?")
    print()
    print("1--> Create New Bank Account")
    print("2--> Modify Bank Account")
    print("3--> Deposit Money")
    print("4--> Withdraw Money")
    print("5--> Show Account Details")
    print("6--> Show Details of All the Accounts")
    task = input("Choose Task from the list:  ")
    
    print()
    if not task=='100':
        if task == '1':
            new_account()
            clear()
        elif task == '2':
            Account_list[working_Account()].modify_account()
            Continue_1()
                
        elif task == '3':
            Account_list[working_Account()].deposit()
            Continue_1()

        elif task == '4':
            Account_list[working_Account()].withdraw()
            Continue_1()

        elif task == '5':
            Account_list[working_Account()].show_account()
            Continue_1()

        elif task == '6':
            Data_tb_form()
            Continue_1()

        else:
            print("Please give valid input..")
            Continue_1()
    else:
        clear()
        print("Glad  to  Help  :-)")
        time.sleep(1)
        clear()
        break