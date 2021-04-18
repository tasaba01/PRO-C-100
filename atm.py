class atm():
    def __init__(CashWithdrawl, BalanceEnquiry):
        self.CashWithdrawl=CashWithdrawl
        self.BalanceEnquiry=BalanceEnquiry
    def withdrawl(self):
        print("withdrawl")
    def balance(self):
        print("$1200")
ord=atm("You have 1200 dollars as your limit","You have 10,000 dollars")
print(ord.BalanceEnquiry)