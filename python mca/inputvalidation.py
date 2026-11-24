import re

email = input("Enter email address: ")

phone = input("Enter phone number: ")

log = input("Enter transaction log: ")

email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'

phone_pattern = r'^[6-9]\d{9}$'

transaction_pattern = r'TXN\d+'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

transaction_ids = re.findall(transaction_pattern, log)

print("Transaction IDs:", transaction_ids)