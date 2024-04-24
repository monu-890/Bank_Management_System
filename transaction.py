class Transaction:
    def __init__(self,transaction_id,account,transaction_type,amount):
        self.transaction_id=transaction_id
        self.account=account
        self.transaction_type=transaction_type
        self.amount=amount