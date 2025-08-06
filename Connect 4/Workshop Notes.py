# String (text)
name = "Carmen"

# Integer
STEPUP_Cohort = 31

# Float
GPA = 0

# List
full_time_mentors = ["Kenzo", "Alex"]

# Operators

money = 0
money = money + 10
money = money - 4
money = money * 4
money = money / 2
money = money % 7 # Modular Division
money = money // 2 # Floor Division
money = money ** 2 # Potential

money = 0
money +- 10 # shorthand add integers (money == 10)

text = "STEP"
text += "UP" # shorthand concat strings (text == "STEPUP")

mentors = ["Kenzo", "Alex"]
mentors += "I'yanna" # shorthand insert in list

name = input() # Input for strings
print (name)

age = int(input()) # Transform input into an int
print(age)

print(f"Hello, {name}") # fString allows variables in text

print(name, end="!") # doesn't create newline
print(age)

#conditionals

if grade> 90: # checks if condition is met
    print ("A")

elif grade > 80: # equivalent of an else if
    print ("B")

else: # nothing else
    print ("C")

if day == "Saturday" or day == "Friday": # or conditional
    print ("No room curfew!")

if time > 22 and day == "Saturday": # and conditional
    print ("Who is up stepping it?")

if "corporate" in events: # if item in list
    print ("Lock in")

# Loops

list = ["Chicken", "Burger", "Jaffe"]
for item in list:
    print (item)

for number in range(10):
    print (number)

number = 0
while True:
    if number == 6 or number == 7:
        break
    number += 1

# Functions
def define_bald(mentor_name: String) -> bool:
    if mentor_name == "Arod":
        return True
    else:
        return False

define_bald("Tommy")

# Arrays/Lists
# Lists are 0-indexed, always [row][column]
mentors = ["Kenzo", "Alex"]
# mentors[0] == "Kenzo"
# mentors[1] == "Alex"
table = [[1,2,3],[4,5,6],[7,8,9]]
table = [[1,2,3]
         [4,5,6]
         [7,8,9]]
# table [0][0] == 1
# table [1][0] == 4
# table [0][1] == 1

# Make connect 4 project in findfour.py module