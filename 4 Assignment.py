# -------------------------------
# 1. Employee Management
# -------------------------------
employees=[]
def add_employee():
    employees.append({"name":input("Name:"),"age":int(input("Age:")),"role":input("Role:"),"salary":float(input("Salary:"))})
def display(): print(employees)
def delete_employee(n): 
    global employees
    employees=[e for e in employees if e["name"]!=n]
add_employee(); display(); delete_employee(input("Delete:")); display()

# -------------------------------
# 2. Student Report Card
# -------------------------------

def report():
    name = input("Name: ")
    m1 = int(input("Sub1: "))
    m2 = int(input("Sub2: "))
    m3 = int(input("Sub3: "))
    
    total = m1 + m2 + m3
    avg = total / 3
    
    grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"
    
    print(f"{name} | Total: {total} | Avg: {avg:.2f} | Grade: {grade}")

report()

# -------------------------------
# 3. Shopping Cart
# -------------------------------

cart = []

def add():
    name = input("Item: ")
    price = float(input("Price: "))
    qty = int(input("Qty: "))
    cart.append({"name": name, "price": price, "qty": qty})

def total():
    bill = sum(i["price"] * i["qty"] for i in cart)
    print("Total:", bill)

add()
total()

# -------------------------------
# 4. Login System
# -------------------------------

users = {"admin": "1234", "user": "abcd"}

u = input("Username: ")
p = input("Password: ")

if users.get(u) == p:
    print("Login Success")
else:
    print("Login Failed")

# -------------------------------
# 5. Unique Visitors
# -------------------------------

visitors = set()

for _ in range(3):
    name = input("Visitor: ")
    visitors.add(name)

print("Unique Visitors:", len(visitors))

# -------------------------------
# 6. String Formatter
# -------------------------------

name = input("Name: ")
product = input("Product: ")

print(f"{name} bought {product}")
print(name.ljust(10, "*"))
print(name.rjust(10, "*"))
print(name.center(10, "*"))

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

votes={"A":0,"B":0}
for _ in range(3):
    v=input("Vote:"); 
    if v in votes: votes[v]+=1
print("Winner:",max(votes,key=votes.get))

# -------------------------------
# 9. Course Enrollment
# -------------------------------

students = {}

# Add student
name = input("Enter student name: ")
courses = input("Enter courses (comma separated): ").split(",")
students[name] = courses

# Update courses
update_name = input("Enter student name to update: ")
if update_name in students:
    new_courses = input("Enter new courses (comma separated): ").split(",")
    students[update_name] = new_courses
else:
    print("Student not found")

# Display student details
print("\nStudent Details:")
for name, courses in students.items():
    print(name, "->", courses)

# -------------------------------
# 10. Number Utility
# -------------------------------
# Function to perform all operations

def number_utility(num):
    print("Binary:", bin(num))
    print("Octal:", oct(num))
    print("Hex:", hex(num))
    print("With Commas:", format(num, ","))
    print("Scientific Notation:", format(num, ".2e"))

# Input
num = int(input("Enter a number: "))

# Function call
number_utility(num)
