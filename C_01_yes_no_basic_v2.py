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

# Main routine
while True:
    want_instructions = yes_no("Do you want to see the instructions? ")
    print(f"you chose {want_instructions}")
print("We done")