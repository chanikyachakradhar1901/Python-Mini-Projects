# -------------------------------
# 1. Employee Management
# -------------------------------
employees = []

name = input("Enter employee name: ")
age = input("Enter age: ")
employees.append({"name": name, "age": age})

print("Employees:", employees)


# -------------------------------
# 2. Student Report Card
# -------------------------------
name = input("\nStudent name: ")
m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))

total = m1 + m2 + m3
avg = total / 3

print(name, "Total:", total, "Average:", avg)


# -------------------------------
# 3. Shopping Cart
# -------------------------------
cart = []

item = input("\nEnter item: ")
price = int(input("Price: "))
cart.append({"item": item, "price": price})

total = 0
for i in cart:
    total += i["price"]

print("Cart:", cart)
print("Total:", total)


# -------------------------------
# 4. Login System
# -------------------------------
users = {"admin": "1234"}

u = input("\nUsername: ")
p = input("Password: ")

if u in users and users[u] == p:
    print("Login Success")
else:
    print("Wrong Login")


# -------------------------------
# 5. Unique Visitors
# -------------------------------
visitors = set()

visitors.add(input("\nVisitor 1: "))
visitors.add(input("Visitor 2: "))

print("Unique Visitors:", visitors)


# -------------------------------
# 6. String Formatter
# -------------------------------
name = input("\nEnter name: ")
product = input("Enter product: ")

print(name, "bought", product)
print(name.center(20, '-'))


# -------------------------------
# 7. Bank System
# -------------------------------
balance = 1000

deposit = int(input("\nDeposit: "))
balance += deposit

withdraw = int(input("Withdraw: "))
balance -= withdraw

print("Balance:", balance)


# -------------------------------
# 8. Voting System
# -------------------------------
votes = {}

c1 = input("\nVote 1: ")
c2 = input("Vote 2: ")

votes[c1] = votes.get(c1, 0) + 1
votes[c2] = votes.get(c2, 0) + 1

print("Votes:", votes)


# -------------------------------
# 9. Course Enrollment
# -------------------------------
students = {}

name = input("\nStudent name: ")
course = input("Course: ")

students[name] = course

print("Students:", students)


# -------------------------------
# 10. Number Utility
# -------------------------------
num = int(input("\nEnter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))