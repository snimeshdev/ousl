
class TakeAction:
    def __init__(self):
        self.actions = ("Create new account", "Deposit money", "Withdraw money", "Check the account balance", "Transfer money")
        self.current_activate_action = -1
        self.print_action_menu()

    '''
        print text-based menu for users from user action tuple
    '''
    def print_action_menu(self):
        print("-"*40)
        for action in self.actions:
            print(f"\t[{self.actions.index(action)}] - {action}")
        print("-" * 40)

    '''
        Take action from user
        return: --> if valid --> user selected action ( integer_value, string_value )
                    if it isn't --> loop and get action again         
    '''
    def take_action(self):
        while True:
            try:
                user_action = int(input("Enter your action : "))
                return user_action, self.actions[user_action]
            except IndexError:
                self.print_error("Invalid Action! Try Again.")
            except ValueError:
                self.print_error("Invalid Action! Try Again. | Please enter numerical value.")

    def print_error(self, error):
        print("\n", "-"*40, "\n", error)
        print("", "-"*40, "\n")

    def activate_action(self, action):
        self.current_activate_action = action
        print("\n\t", f"\"{self.actions[self.current_activate_action]}\"", "action has been activated...\n\t [-1] - Exit from current action\n")

    def deactivate_action(self):
        self.current_activate_action = -1

    def take_user_inpt(self, label):
        while True:
            try:
                user_inpt = float(input(label))
                return user_inpt
            except ValueError:
                self.print_error("Invalid value! Try again and enter numerical value...")


class AccountHandler(TakeAction):

    def __init__(self):
        super().__init__()
        self.db = {}

    '''
        create account
    '''
    def create_account(self):
        account_number, initial_amount = None, None
        while True:
            account_number = super().take_user_inpt("Enter new account number : ")
            if account_number == -1:
                return -1
            if not self.check_valid_account(account_number):
                break
            super().print_error("This account already exist! Try another account number.")
        while True:
            initial_amount = super().take_user_inpt("Enter initial deposit(Rs.) : ")
            if initial_amount == -1:
                return -1
            if initial_amount > 0:
                break
            else:
                super().print_error("Value error! please enter positive numerical value")
        self.db.setdefault(account_number, initial_amount)
        super().print_error("Account created successfully...")

    '''
        deposit money
    '''
    def deposit(self):
        account_number, deposit_amount = None, None
        while True:
            account_number = super().take_user_inpt("Enter existing account number : ")
            if account_number == -1:
                return -1
            if self.check_valid_account(account_number):
                break
            super().print_error("Enter valid account number! This account not already exist.")
        while True:
            super().print_error(f"account number  : {int(account_number)}\n account balance : {self.db[account_number]}")
            deposit_amount = super().take_user_inpt("Enter amount of deposit(Rs.) : ")
            if deposit_amount == -1:
                return -1
            if deposit_amount > 0:
                self.db[account_number] += deposit_amount
                super().print_error(f"account number  : {int(account_number)}\n withdraw amount : {deposit_amount}\n new account balance : {self.db[account_number]}")
                super().print_error("Money deposit successfully...")
                break
            else:
                super().print_error("Value error! please enter positive numerical value")

    '''
        withdraw money
    '''
    def withdraw(self):
        account_number, withdraw_amount = None, None
        while True:
            account_number = super().take_user_inpt("Enter existing account number : ")
            if account_number == -1:
                return -1
            if self.check_valid_account(account_number):
                break
            super().print_error("Enter valid account number! This account not already exist.")
        while True:
            super().print_error(f"account number  : {int(account_number)}\n account balance : {self.db[account_number]}")
            withdraw_amount = super().take_user_inpt("Enter amount of withdraw(Rs.) : ")
            if withdraw_amount == -1:
                return -1
            if withdraw_amount > 0:
                if self.db[account_number] < withdraw_amount:
                    super().print_error("Insufficient account balance!")
                else:
                    self.db[account_number] -= withdraw_amount
                    print(self.db[account_number])
                    super().print_error(f"account number  : {int(account_number)}\n withdraw amount : {withdraw_amount}\n new account balance : {self.db[account_number]}")
                    super().print_error("Money withdraw successfully...")
                    break
            else:
                super().print_error("Value error! please enter positive numerical value")

    '''
        check account balance
    '''
    def check_account(self):
        account_number = None
        while True:
            account_number = super().take_user_inpt("Enter existing account number : ")
            if account_number == -1:
                return -1
            if self.check_valid_account(account_number):
                super().print_error(f"account number  : {int(account_number)}\n account balance : {self.db[account_number]}")
                break
            super().print_error("Enter valid account number! This account not already exist.")

    '''
        transfer money
    '''
    def transfer(self):
        account_number, to_witch_account, transfer_amount = None, None, None

        while True:
            account_number = super().take_user_inpt("Enter existing account number : ")
            if account_number == -1:
                return -1
            if self.check_valid_account(account_number):
                super().print_error(f"account number  : {int(account_number)}\n account balance : {self.db[account_number]}")
                break
            super().print_error("Enter valid account number! This account not already exist.")

        while True:
            to_witch_account = super().take_user_inpt("Enter to witch account number : ")
            if to_witch_account == -1:
                return -1
            if self.check_valid_account(to_witch_account):
                super().print_error(f"account number  : {int(to_witch_account)}\n account balance : {self.db[to_witch_account]}")
                break
            super().print_error("Enter valid account number! This account not already exist.")

        while True:
            transfer_amount = super().take_user_inpt("Enter amount of withdraw(Rs.) : ")
            if transfer_amount == -1:
                return -1
            if transfer_amount > 0:
                if self.db[account_number] < transfer_amount:
                    super().print_error("Insufficient account balance!")
                else:
                    self.db[account_number] -= transfer_amount
                    self.db[to_witch_account] += transfer_amount
                    super().print_error(f"account number  : {int(account_number)}\n account balance : {self.db[account_number]}\n transfer amount  : {transfer_amount}\n"
                                        f"\n account number  : {int(to_witch_account)}\n account balance : {(self.db[to_witch_account])}\n transfer amount  : {transfer_amount}")
                    super().print_error("Money withdraw successfully...")
                    break
            else:
                super().print_error("Value error! please enter positive numerical value")

    def check_valid_account(self, account_number):
        if account_number in self.db.keys():
            return True
        else:
            return False


account = AccountHandler()
action_index, action_text = account.take_action()

while True:
    match action_index:
        case 0:
            account.activate_action(action_index)
            if account.create_account() == -1:
                account.deactivate_action()
                account.print_action_menu()
                action_index, action_text = account.take_action()
                continue
        case 1:
            account.activate_action(action_index)
            if account.deposit() == -1:
                account.deactivate_action()
                account.print_action_menu()
                action_index, action_text = account.take_action()
                continue
        case 2:
            account.activate_action(action_index)
            if account.withdraw() == -1:
                account.deactivate_action()
                account.print_action_menu()
                action_index, action_text = account.take_action()
                continue
        case 3:
            account.activate_action(action_index)
            if account.check_account() == -1:
                account.deactivate_action()
                account.print_action_menu()
                action_index, action_text = account.take_action()
                continue
        case 4:
            account.activate_action(action_index)
            if account.transfer() == -1:
                account.deactivate_action()
                account.print_action_menu()
                action_index, action_text = account.take_action()
                continue
