from finance import BankAccount

a = BankAccount("Alex", "1111", 1000)
b = BankAccount("Ivan", "2222", 200)

a.deposit(500)
a.transfer(b, 300)
a.show()
b.show()

try:
    a.withdraw(99999)
except ValueError as e:
    print(e)

try:
    a.balance = -5
except ValueError as e:
    print(e)