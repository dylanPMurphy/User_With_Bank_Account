from bank_account import BankAccount


class User:
    import bank_account
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # adding the deposit method
    def make_deposit(self, amount):	                            # takes an argument that is the amount of the deposit
        self.account.deposit(amount)	                        # the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):                           ## this method decrease the user's balance by the amount specified
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):                              #-  method print the user's name and account balance to the terminal
        print("User: %s --- Balance: %.2f" % (self.name, self.account.balance))                                                   
        return self
    def transfer_money(self, other_user, amount):                # -  method decrease the user's balance by the amount and add that amount to other other_user's balance
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self


def testCases():
    user1 = User('doug', 'doug@doug.com')
    #user2 = User('fran', 'fran@fran.fran')
    #user3 = User('reg','reggie@reg.com')

    user1.make_deposit(200)
    user1.display_user_balance()
    user1.account.yeildInterest()
    user1.display_user_balance()

#     user1.make_deposit(231)
#     user1.display_user_balance()

#     user1.make_deposit(12231)

#     user1.display_user_balance()


#     user2.make_deposit(22331)
#     user2.make_deposit(231)
#     user2.display_user_balance()

#     user2.make_withdrawal(213)
#     user2.make_withdrawal(2123)
#     user2.display_user_balance()

#     user3.make_deposit(231211)
#     user3.make_withdrawal(213)
#     user3.make_withdrawal(213)
#     user3.make_withdrawal(213)
#     user3.display_user_balance()


#     user4 = User('zeus', 'lordofthunda@olympus.gods')
#     user4.make_deposit(2342).make_deposit(123186723).make_withdrawal(12387).display_user_balance().make_withdrawal(234524).display_user_balance()
testCases()