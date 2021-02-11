# import statements


# functions go here


# ***** Main Routine *****

# Set up directories / lists needed to hold date

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket detials

name = " "
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    if count < 4:
        print ("You have {} seats "
            "left".format (MAX_TICKETS - count))

    # Warns user that only one is left!
    else:
            print("*** There is ONE seat left!! ***")

    # Get details...

    # Get name (can't be blank)
    name = input ("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "there are {} places still available"
          .format(count, MAX_TICKETS - count))



  # Get age (between 12 and 130)

  # Calculate ticket price

  # Loop to ask for snacks

  # Caluclate snack price

  # Ask for payment method (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file