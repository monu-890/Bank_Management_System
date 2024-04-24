from account_management.account import Account 
from account_management.customer import Customer 
from transaction_processing.transaction import Transaction 
from transaction_processing.transaction_processor import TransactionProcessor 

# create customers
customer1=Customer("C001","Abhang Karode")
customer2=Customer("C002","Pooja Surawar")
customer3=Customer("C003","Nishid Jojare")

# create accounts
account1=Account("A001",customer1)
account2=Account("A002",customer2,balance=500.0)
account3=Account("A003",customer3,balance=2000)

# display initial balance
print(f"{customer1.name}'s Balance : {account1.get_balance()}")
print(f"{customer2.name}'s Balance : {account2.get_balance()}")
print(f"{customer3.name}'s Balance : {account3.get_balance()}")
print()

# perform transactions
transaction1=Transaction("T001",account1,"deposit",1000.0)
transaction2=Transaction("T002",account2,"withdraw",150.0)
transaction3=Transaction("T003",account3,"withdraw",1000)

TransactionProcessor.process_transaction(transaction1)
TransactionProcessor.process_transaction(transaction2)
TransactionProcessor.process_transaction(transaction3)

# display updated balances
print(f"{customer1.name}'s Updated Balance : {account1.get_balance()}")
print(f"{customer2.name}'s Updated Balance : {account2.get_balance()}")
print(f"{customer3.name}'s Updated Balance : {account3.get_balance()}")
print()


# showing message for Invalid transaction type
transaction3=Transaction("T003",account3,"do withdraw",1000.0)
TransactionProcessor.process_transaction(transaction3)


# showing message for insufficient funds 
transaction3=Transaction("T003",account3,"withdraw",3000)
TransactionProcessor.process_transaction(transaction3)



