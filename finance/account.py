class BankAccount:
    def __init__(self, owner, number, balance=0):
        self.__owner = owner
        self.__number = number
        self.__balance = 0
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума має бути більше нуля")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            raise ValueError("Невірна сума")
        self.__balance -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def show(self):
        print(self.__owner, self.__number, self.__balance)