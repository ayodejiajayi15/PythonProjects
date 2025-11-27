import random

password = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{:"?><'

password_length = int(input('Enter Password Length:'))

a = "".join(random.sample(password, password_length))

print(f"Your password is: {a}")