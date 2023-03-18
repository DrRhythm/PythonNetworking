#!/usr/bin/python

ip_addr = input("Enter an IP Address: ")

octets = ip_addr.split(".")
int_oct1 = int(octets[0])
int_oct2 = int(octets[1])
int_oct3 = int(octets[2])
int_oct4 = int(octets[3])

#print(int_oct1)
print("\n")
print("-" * 80)
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int_oct1), bin(int_oct2), bin(int_oct3), bin(int_oct4)))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int_oct1), hex(int_oct2), hex(int_oct3), hex(int_oct4)))
print("-" * 80)