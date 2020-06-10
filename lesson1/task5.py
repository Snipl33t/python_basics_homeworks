# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

In this task we are dealing with company's financial status. You will be asked to enter revenue and costs of the the 
company. 
The program will tell you the financial status and whether the company is profitable or not. After that you 
will be asked to type the amount of employees, according to that the company's profit by one employee will be 
given.\n """

# Greet user
print(welcome_string)

# Ask user to enter revenue
revenue = input("Enter revenue: ")

# Check if user typed an integer value. If not, then ask again
while not revenue.isdigit():
    revenue = input("Please, enter an integer variable! Should be a simple number\n")

# Ask user to enter costs
costs = input("Enter costs: ")

# Check if user typed an integer value. If not, then ask again
while not costs.isdigit():
    costs = input("Please, enter an integer variable! Should be a simple number\n")

# After the checking process we can safely make strings into integers
revenue = int(revenue)
costs = int(costs)

# Compare revenue and costs
if revenue > costs:
    # If revenue is higher, then display the following
    print(f"Company is profitable.")

    # Calculate profitability
    profitability = revenue // costs

    # Display the result
    print(f"Company's profitability is {profitability}.")

    # Ask user to enter number of employees
    num_emp = input("Enter the number of employees: ")

    # Check if user typed an integer value. If not, then ask again
    while not num_emp.isdigit():
        num_emp = input("Please, enter an integer variable! Should be a simple number\n")

    # After the checking process we can safely make a string into integer
    num_emp = int(num_emp)

    # Calculate the revenue per employee
    revenue_per_emp = revenue // num_emp

    # Display the result
    print(f"Revenue per employee is {revenue_per_emp}.")

else:
    # If revenue is lower, then display the following
    print(f"Company is unprofitable.")
