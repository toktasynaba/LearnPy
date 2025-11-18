from datetime import datetime

print("Hi, you are taking a survey!")

name = str(input("Enter your name: "))
first_name = str(input("Enter your last name: "))
birth = int(input("Enter your year of birth: "))
question_1 = str(input("Do you like this course?: "))
question_2 = str(input("What are you expecting from the course?: "))

current_year = datetime.today().year
print()
print(f"Your name is {name}")
print(f"Your last name is {first_name}")
print(f"You are {current_year - birth} years old")
print(f"Your answer to question 1 is: {question_1}")
print(f"Your answer to question 2 is: {question_2}")