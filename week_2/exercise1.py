#!/usr/bin/python
# open the show_version.txt file
# use the read() method to read in the file
# print file contents and type of variable to screen
# close file

file = open("show_version.txt")
output = file.read()
print(output)
file.close()

# Do the same in python context manager