import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('number of passwords?')
number = int(number)

length = input('password length?')
length = int(length)

print('\npasswords:')

for x in range(number):
  password = ''
  for y in range(length):
    password += random.choice(chars)
  print(password)