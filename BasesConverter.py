# v0.0.1 - Write from scratch | No AI | Author: XIII___ (XIII-MC)
# Sources used:
# - https://www.datacamp.com/tutorial/python-data-type-conversion
# - https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output
# - https://stackoverflow.com/questions/11806559/removing-first-x-characters-from-string
# Made for CASIO Graph 90+E | 3.8

# Make this always run
while True:

    try:

        # Get user input
        print("'0x' for hexadecimal")
        print("'0b' for binary")
        user_input = input("Enter value: ")

        # Parse according to base.
        if user_input.startswith("0x"):
            num = int(user_input, 16)
        elif user_input.startswith("0b"):
            num = int(user_input, 2)
        else:
            num = int(user_input)

        # Print out our results
        print("======= Base =======")
        print("D:", num)
        print("B:", bin(num)[2:])
        print("H:", hex(num)[2:].upper())
        print("====================")

        print(input("Continue? ").upper())

    # If our hexadecimal value is outside the 0-F range.
    except ValueError:
        print("Please enter a valid value.")

    # The 'AC' key does that.
    except KeyboardInterrupt:
        break