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

    try:

        # Get IPv4 input and split each octet.
        ipv4_input = input("IP: ")
        list_ipv4_input = list(ipv4_input.split('.', 4)) # split at '.', max 4 for ipv4 (ipv6 is a big nono here).

        # Check if there's 4 octet, if not: exit.
        if len(list_ipv4_input) != 4:
            print("Invalid IPv4 address")
            break

        # Check if we only got integers (as strings), if we do, continue.
        if all([item.isdigit() for item in list_ipv4_input]):

            # Lists used for easier converting and output.
            ip_bin = []
            ip_hex = []

            for octet in list_ipv4_input:

                # Prevent invalid IPv4
                if (octet > '255') | (len(octet) > 3):
                    print("Invalid IPv4 address")
                    break

                ip_bin.append(int_to_bin(int(octet)))
                ip_hex.append(int_to_hex(int(octet)))

            # Show binary and hexadecimal forms (basic).
            print("======= Base =======")
            for i in range(0, len(ip_bin), 2):
                print(" ".join(ip_bin[i:i + 2]))
            print(*ip_hex)

            print("====================")

            print(input("Continue? ").upper())

    # The 'AC' key does that.
    except KeyboardInterrupt:
        break
