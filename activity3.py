# initialize answer and price
answer = "y"
price = 0
# enter 'while' loop
while answer is "y":
    print("You will be asked the number of board feet for the purchase and the type of lumber (common or select)")
    # collect input and calculate price
    try:
        # collect length input
        length = float(input("Enter number of board feet:       "))
        # check if input is positive
        if int(length) > 0:
            # collect lumber type
            lumber_type = int(input("Enter a 1 for select lumber or a 2 for common lumber  "))
            # calculate price
            if lumber_type == 1:
                price = length * 2
            elif lumber_type == 2:
                price = length
            # catch bad input for price
            else:
                print("Wrong input!")
            # calculate discount
            if 9999 < price < 50000:
                price = price * .9
            if price >= 50000:
                price = price * .8
        # catch negative input for length
        else:
            print("Wrong input!")
    # catch non-numeric input for length
    except ValueError:
        print("Wrong input!")
        answer = "y"
    # print total
    print("Total price for the lumber is: ", price)
    # prompt to continue
    answer = str(input("\nContinue (y/n)?: "))
    # end loop
    if answer is "n":
        break
    # catch bad string input for 'Continue' prompt
    elif answer is not "y":
        print("Wrong input!")
        answer = str(input("\nContinue (y/n)?: "))
# exit message
print("Exiting program...")
