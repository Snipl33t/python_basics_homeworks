# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

In this task I would like you to enter time in seconds.
The output is given in the following format: "hh:mm:ss".\n"""

# Greet user
print(welcome_string)

# Ask user to enter time in seconds
time = input("Enter time in seconds: ")

# Check if user typed an integer value. If not, then ask again
while not time.isdigit():
    time = input("Please, enter an integer variable! Should be a simple number\n")

# After the checking process we can safely make a string into integer
time = int(time)

# Calculate time for a given format
minutes = time // 60 % 60
hours = time // 3600
seconds = time % 60

# Bring the calculated time to a given format
# If hours/minutes/seconds are less then 10, then add 0 in the front (e.g. if hours = 1, make it 01)
if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

# Display time
print(f'Time in the regular "human" format: {hours}:{minutes}:{seconds}')
