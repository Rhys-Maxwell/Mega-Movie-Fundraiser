# Valid snack holds list of all snacks
# Each item in valid snacks is a list with valid options for each snack <full name, letter code (a - e)
# and possible abbreviations eto>

def string_check(choice, options):

    for var_list in options:


        # if the snack is in one of the lists, return the full snack name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

            # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

check_snack = "invalid choice"



while check_snack == "invalid choice":
    want_snack = input ("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# if they say yes, ask what snacks the want (and add to our snack_order list)
if check_snack == "Yes:":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desired_snack = input ("Snack: ").lower()

        if __name__ == '__main__':
            if desired_snack == "xxx":
                break

                # check if snack is valid
                snack_choice = string_check(desired_snack, valid_snacks)
                print("Snack Choice ", snack_choice)

                # add snack to list..

                # check that snack is not the exit code before adding
                if snack_choice != "xxx" and snack_choice != "invalid choice":
                    snack_order.append(snack_choice)



for item in range(0, 6):

    # ask user for desired snack and put it in lowercase
    desired_snack = input("snack: ").lower()

    # check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice: ", snack_choice)

