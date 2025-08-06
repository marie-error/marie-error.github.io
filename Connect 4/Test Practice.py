# Ask the user for their name and how many days they have left of STEPUP using input and int(input())
# Subtract a day from the days left
# Print a message mentioning: "Hi {name}, you have {days_left} days left in STEPUP! We will miss you!"

print ("Hello! What is your name?")
name = input()
print ("How many days are left in STEPUP?")
days_left = int(input())
print (f"Hi {name}, you have {days_left} days left in STEPUP! We will miss you!")
days_left = days_left - 1

# Make a program using conditionals and inputs that asks "Are you Up Stepping it?" expecting an answer
# Print a happy emoji like :D if the answer is y or yes or im up, otherwise, print angry emoji like X(
print ("Are you Up Stepping it?")
answer = input()
if answer == "yes" or answer == "y" or answer == "im up":
    print (":D")
else:
    print ("X(")

# Practice 3
# Print "thank you " at least 3 times
# Print a list of all the full-time mentors' names: ["Kenzo", "Alex", "Arod", "Tommy", "Daniela", "Madrona"]

for i in range(3):
    print ("Thank you")

mentors_full_time = ["Kenzo", "Alex", "Arod", "Tommy", "Daniela", "Madrona"]
for mentor in mentors_full_time:
    print (mentor)
