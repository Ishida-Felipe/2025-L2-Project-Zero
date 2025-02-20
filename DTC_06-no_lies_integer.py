# Functions
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Return the response if it`s an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main Routine

while True:
    print()

    user_name = input("Name: ") # replace with call to 'not blank' function!

    # Ask for their age and check it`s between 12 and 120
    user_age = int_check("Age: ")

    # Output error message / sucess message
    if user_age < 12:
        print(f"{user_name} is too young")
        continue
    elif user_age > 120:
        print(f"{user_name} is too old")
        continue
    else:
        print(f"{user_name} bought a ticket")
