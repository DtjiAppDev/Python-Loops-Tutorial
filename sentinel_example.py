# Sentinel Example


from decimal import Decimal


def is_number(string: str) -> bool:
  try:
    Decimal(string)
    return True
  except:
    return False


# The following sentinel will ensure that you key in a number
n: str = input("Please enter a number: ")
while not is_number(n):
  n = input("Not a number! Please try again! ")


print("Your number is = " + str(n))
