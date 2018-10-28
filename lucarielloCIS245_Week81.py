#!/usr/bin/python3
"""

__author__ = "Brandon Lucariello"
__copyright__ = "cc"
__credits__ = ["Brandon Lucariello"]
__license__ = "cc"
__version__ = "0.1"
__maintainer__ = "Brandon Lucariello"
__email__ = "blucariello@my365.bellevue.edu"
__status__ = "testing"


"""

class BankAccount:
	
	def __init__(self, accountNum, balance):
		self.accountNum = accountNum
		self.balance = balance

		
	#def withdrawl():
		#pass
		
	#def deposit():
		#pass
		
	#def getBal():
		#pass
		
		
class CheckingAccount(BankAccount):

	def __init__(self, fees, minBal):
		self.fees = fees
		self.minBal = minBal
		super().__init__(self)
		
	#def deductFees(self):
		#pass
		
	#def checkMinBal(self):
		#pass
	
	
#class SavingsAccount(BankAccount):

	#def __init__(self, intRate = 1.02):
		#self.intRate = intRate
		#super().__init__(self)
		
		
	#def addInterest(self):
		#pass

		
account_1 = BankAccount(1,100)
account_2 = BankAccount(2,25)

#checking_1 = CheckingAccount(5,50)

#savings_1 = SavingsAccount()


#print(checking_1.balance)

print(account_1.balance)


