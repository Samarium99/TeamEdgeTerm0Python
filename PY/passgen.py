import random
# Define sets of characters for different password categories
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
digits = "0123456789"
symbols = "!@#$%^&*()"
# Combine all character sets
all_chars = lowercase_letters + uppercase_letters + digits + symbols
# Set password length
password_length = 24
# Generate a random password
password = "".join(random.sample(all_chars, password_length))
# Print the generated password
print(password)