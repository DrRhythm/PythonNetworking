#!/usr/bin/python

# Create a list of 5 IPs
ip_list = ["10.1.2.4", "172.16.15.9", "154.69.45.26", "10.5.7.1", "10.7.96.5"]
print(ip_list)
# use append to add an ip to the end of the list
ip_list.append("192.65.8.2")
print(ip_list)
# user extend to add two more ips to the end
new_ips = ["192.168.1.1", "192.168.1.2"]
ip_list.extend(new_ips)
print(ip_list)
# print the list, print the first ip and print the last ip
print(ip_list[0])
print(ip_list[-1])
# use pop to remove the first and last ip in the list
ip_list.pop(0)
ip_list.pop(-1)
# update the first ip in the list to 2.2.2.2, print out the new first ip
ip_list.insert(0, "2.2.2.2")
print(ip_list[0])