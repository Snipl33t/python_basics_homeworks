# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

The athlete does running everyday. In the first day his result was 'a' kilometers. Everyday he improved his results 
by 10%.
It is required to find the day, when athletes result is not less than 'b' kilometers.\n """

# Greet user
print(welcome_string)

# Ask user to enter a
a = input("Enter a in km: ")

# Check if user typed an integer value. If not, then ask again
while not a.isdigit():
    a = input("Please, enter an integer variable! Should be a simple number\n")

# Ask user to enter b
b = input("Enter b in km: ")

# Check if user typed an integer value. If not, then ask again
while not b.isdigit():
    b = input("Please, enter an integer variable! Should be a simple number\n")

# After the checking process we can safely make strings into integers
a = int(a)
b = int(b)

# Initial day is 1
day = 1
# While his result is smaller than his goal
while a < b:
    # Increase his result by 10% with each day
    a *= 1.1
    day += 1

# Display the result
print(f"On day {day}, the athlete achieved his result - not less than {b} km.")
