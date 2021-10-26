"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Danyah Harris
Date:   November 3, 2020
"""

import currency

soruce = input("3-letter code for original currency: ")

destintation = input("3-letter code for the new currency: ")
amount = float(input("Amount of the original currency: "))

intial_value = currency.exchange(soruce,destintation, amount)
output_value = round(intial_value,3)
y = str(output_value)
x = str(amount)

print('You can exchange ' + x +' '+soruce+' for ' +y+' '+destintation+'.')