# Get input from the user
decimal_input = input("Enter the Parameter Number as decimal number without the P (e.g.P13.02  = 13.02 ): ")

# Split the input at the decimal point
whole_part, fractional_part = decimal_input.split('.')

# Convert the whole part to an integer and then to hexadecimal
whole_part_hex = f"{int(whole_part):02X}"
fractional_part_hex= f"{int(fractional_part):02X}"

# Print the results
print(f"Parameter {decimal_input} is in EEPRom Register 0x{whole_part_hex}{fractional_part_hex}")
