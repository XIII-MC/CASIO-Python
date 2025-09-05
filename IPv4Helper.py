# v0.0.1 - Rewrite from scratch | No AI | Author: XIII___ (XIII-MC)
# Sources used:
# - StackOverflow
# - w3schools.com
# - datascienceparichay.com
# Made for CASIO Graph 90+E | 3.8

# Helper functions.

# Convert an Integer to binary.
def int_to_bin(integer):
   return '{0:08b}'.format(integer)

# Convert an Integer to hexadecimal
def int_to_hex(integer):
   return '{0:x}'.format(integer).upper()

# Make this always run
while True:

    # Get IPv4 input and split each octet.
    ipv4_input = input("IP: ")
    split_ipv4_input = ipv4_input.split('.', 4) # split at '.', max 4 for ipv4 (ipv6 is a big nono here).

    # Check if there's 4 octet, if not: exit.
    if len(split_ipv4_input) != 4:
        print("Invalid IPv4 address")
        break

    # Check if we only got integers (as strings), if we do, continue.
    if all([item.isdigit() for item in split_ipv4_input]):

        # We're gonna use these often so we might as well define them here.
        ipv4_octet_1 = split_ipv4_input[0]
        ipv4_octet_2 = split_ipv4_input[1]
        ipv4_octet_3 = split_ipv4_input[2]
        ipv4_octet_4 = split_ipv4_input[3]

        ipv4_octet_1_int = int(split_ipv4_input[0])
        ipv4_octet_2_int = int(split_ipv4_input[1])
        ipv4_octet_3_int = int(split_ipv4_input[2])
        ipv4_octet_4_int = int(split_ipv4_input[3])

        # Last check, verify if the numbers aren't above 255.
        if ((ipv4_octet_1_int > 255 | len(ipv4_octet_1) > 3)
                | (ipv4_octet_2_int > 255 | len(ipv4_octet_2) > 3)
                | (ipv4_octet_3_int > 255 | len(ipv4_octet_3) > 3)
                | (ipv4_octet_4_int > 255 | len(ipv4_octet_4) > 3)):
            print("Invalid IPv4 address")
            break

        # Pre-"calculate" everything here
        ipv4_octet_1_binary = int_to_bin(ipv4_octet_1_int)
        ipv4_octet_2_binary = int_to_bin(ipv4_octet_2_int)
        ipv4_octet_3_binary = int_to_bin(ipv4_octet_3_int)
        ipv4_octet_4_binary = int_to_bin(ipv4_octet_4_int)

        ipv4_octet_1_hex = int_to_hex(ipv4_octet_1_int)
        ipv4_octet_2_hex = int_to_hex(ipv4_octet_2_int)
        ipv4_octet_3_hex = int_to_hex(ipv4_octet_3_int)
        ipv4_octet_4_hex = int_to_hex(ipv4_octet_4_int)

        # Show binary and hexadecimal forms
        print(ipv4_octet_1_binary, ipv4_octet_2_binary, ipv4_octet_3_binary, ipv4_octet_4_binary)
        print(ipv4_octet_1_hex, ipv4_octet_2_hex, ipv4_octet_3_hex, ipv4_octet_4_hex)

        if input("Continue? [y/n]: ").upper() != "Y":
            break
