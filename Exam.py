Prompt the user for their name
name = input("What is your name? ")

# Check the length of the name and print a different message depending on its length
if len(name) < 5:
    print("Your name is short!")
elif len(name) < 10:
    print("Your name is medium length.")
elif len(name) < 15:
    print("Your name is quite long!")
else:
    print("Your name is really long!")


Create a list of strings
strings = ["apple", "banana", "cherry", "grape", "watermelon"]

Loop over the list and print every other string, along with a message indicating whether the loop is even or odd
for i in range(len(strings)):
    if i % 2 != 0:
        continue
    if i % 4 == 0:
        print("Even loop:", strings[i])
    else:
        print("Odd loop:", strings[i])


Define the math problem
num1 = 9
num2 = 6
operator = '/'
correct_answer = num1 / num2

# Ask the user for there answer until they get it right
while True:
    # Ask the user for their answer
    user_answer = int(input(f"What is {num1} {operator} {num2}? "))

    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Congratulations, you got it right!")
        break
    else:
        print("Sorry, that's not the right answer. Please try again.")


Define the function
def getfirstname():
    while True:
        # Ask the user for their first name
        first_name = input("Please enter your first name: ")

        # Check if the first name includes any numbers
        if any(char.isdigit() for char in first_name):
            print("Sorry, your first name cannot include any numbers. Please try again.")
            continue
        else:
            break
    
    return first_name
