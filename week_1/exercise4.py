#!/usr/bin/python

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
split_version = show_version.split()
model_number = split_version[1]
serial_number = split_version[2]

# Remove all leading and trailing whitespace from string
strip_version = show_version.strip()
#print(strip_version)
#print(show_version)
# Split the string and extract the model and serial number
# print(split_version)
# print(model_number)
# Check if 'Cisco'/check if 881 is in the model string
if "cisco" in model_number.lower() and "881" in model_number:
    print(model_number)
else: 
    print("Model not found")    
# Print the serial number and model
print(serial_number)