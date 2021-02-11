# Functions go here


def not_blank (question, error_message):
    valid = False

    while not valid:
        response = input (question)

        if response != "":
            return response

        else:
            print (error_message)


# Main Routine goes here
name = not_blank("name: ",
                 "sorry - this cant be blank, "
                 "please enter your name")




