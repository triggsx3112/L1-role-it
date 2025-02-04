# Functions go here
def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter a yes / no")


def instructions():

    print("""
 ***instructions***
 
 Roll the dice and try to win!   
    """)


# Main routine
want_instructions = yes_no("Do you want to see the instructions? ")
print(f"you chose {want_instructions}")

# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

print()
print("Program continues")