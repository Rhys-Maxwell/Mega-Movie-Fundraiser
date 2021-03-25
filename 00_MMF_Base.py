# import statements


# functions go here

# ***** Main Routine *****
def not_blank (question):
    valid = False

    while not valid:
        response = input (question)

        # If name is not blank, program continues
        if response != "":
            return response

        # If name is blank, show error (repeat & loop)
        else:
            print ("sorry - this cant be blank")

# checks for an integer more than 0
def int_check(question):
    error = "Please  enter a whole number"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print (error)
            else:
                return response


                # if an integer is not entered, display an error
        except ValueError:
            print(error)


# ******** Main Routine ********

# Set up directories / lists needed to hold date

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket detials

# start of loop

# Initialise loop so that it runs atleast once

MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0


while name != "xxx" and ticket_count < MAX_TICKETS:

    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    else:
        print("*** You have one seat left ***")

    # Get details...

    # Get name (can't be blank)
    name = not_blank("Name? ")

# End of tickets loop

    if name == "xxx":
        # print("You have sold {} tickets.) \n"
        #       "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))
        break

    # Get age (between 12 & 130)
    age = int_check("Age: ")

    # check that age is valid (between 12 & 130)
    if age < 12:
        print("Sorry, you are too young to view this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

    if ticket_count == MAX_TICKETS:
        print("You have sold all the available tickets!")

  # Calculate ticket price
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they unsold tickets...

if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.   \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))

  # Loop to ask for snacks


  # Caluclate snack price

  # Ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file