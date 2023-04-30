
class Account:

    def __init__(self, filepath):
        self.f_path = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.f_path, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    """This class generates checking account objecs."""
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


jacks_checking = Checking("jacks.txt", 1)
jacks_checking.transfer(10)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

johns_checking = Checking("johns.txt", 1)
johns_checking.transfer(10)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)
