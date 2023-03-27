#!/usr/bin/python
from pprint import pprint

# Use redlines to open show_arp.txt, use slice to remove header
arp = open("show_arp.txt")
output = arp.readlines()


# Use pretty print to print out the resulting list
pprint(output[1:])

# Use the sort method to sort the list by IP
# Couldn't get this to work but there is a PR for his repo to fix this exercise? Look into later. 
output.sort()
# print(output)

# Create a new list slice that is only the first three ARP entries
arp_list = output[:3]

# Use join to put these ARP entries together as a single string with '\n' as the separator
arp_list = "\n".join(arp_list)

# Write the string to a file named arp_entries.txt
with open("arp_entries.txt", "w") as file:
    file.write(arp_list)