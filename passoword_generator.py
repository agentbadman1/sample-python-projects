# password generator

import random

password ='''abcsefghijklmnopqrstuvwxyzABCSEFGHIJKLMNOPQRSTUVWXYZ012345678!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

pass_length = int(input('Enter the lenght of the password u want: '))

a = "".join(random.sample(password,pass_length))

print(f"Your password is: {a}")