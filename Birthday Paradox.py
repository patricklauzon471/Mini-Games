# The birthday paradox is the probability that two people will have the same birthday even in a small group
# In a group of 70 people there is a 99.23% chance two people have matching birthdays
# In a group of 23 people there's a 50% chance of a matching birthday
# This is a Monte Carlo experiment

# Birthday paradox math
# p(n) = 365!/((365^n)*[(365-n)!])
# the input n is the amount of people in the room

from math import factorial


people = 0
people = int(input('How many people are in the room '))

equation = factorial(365)/((365**people)*(factorial(365-people)))

print('The percent chance that two people in the room share the same birthday is')
print(100 - equation*100)
