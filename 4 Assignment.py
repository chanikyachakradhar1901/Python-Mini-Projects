# -------------------------------
# 1. Employee Management
# -------------------------------
employees = []

def add_employee():
    emp = {
        "name": input("Name: "),
        "age": int(input("Age: ")),
        "role": input("Role: "),
        "salary": float(input("Salary: "))
    }
    employees.append(emp)

def update_employee():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["age"] = int(input("New Age: "))
            emp["role"] = input("New Role: ")
            emp["salary"] = float(input("New Salary: "))
            print("Updated Successfully")
            return
    print("Employee not found")

def delete_employee():
    name = input("Enter name to delete: ")
    global employees
    employees = [e for e in employees if e["name"] != name]

def display():
    print("\nEmployees:")
    for emp in employees:
        print(emp)

# Run once
add_employee()
update_employee()
delete_employee()
display()

# -------------------------------
# 2. Student Report Card
# -------------------------------

student = {}

def report():
    student["name"] = input("Name: ")
    student["marks"] = [
        int(input("Sub1: ")),
        int(input("Sub2: ")),
        int(input("Sub3: "))
    ]
    
    total = sum(student["marks"])
    avg = total / 3
    
    grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"
    
    print(f"\nName: {student['name']}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")

report()

# -------------------------------
# 3. Shopping Cart
# -------------------------------

cart = []

def add_item():
    item = {
        "name": input("Item: "),
        "price": float(input("Price: ")),
        "qty": int(input("Quantity: "))
    }
    cart.append(item)

def remove_item():
    name = input("Enter item to remove: ")
    global cart
    cart = [i for i in cart if i["name"] != name]

def display():
    print("\nCart Items:")
    for i in cart:
        print(i)

def total():
    bill = sum(i["price"] * i["qty"] for i in cart)
    print("Total Bill:", bill)

# Run once
add_item()
remove_item()
display()
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

# Create account
account = {
    "name": input("Enter name: "),
    "balance": float(input("Enter initial balance: "))
}

# Deposit function
def deposit(amount):
    account["balance"] += amount

# Withdraw function
def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
    else:
        print("Insufficient balance")

# Check balance function
def check_balance():
    print("Current Balance:", account["balance"])

# Perform operations
deposit(float(input("Enter deposit amount: ")))
withdraw(float(input("Enter withdraw amount: ")))
check_balance()

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
