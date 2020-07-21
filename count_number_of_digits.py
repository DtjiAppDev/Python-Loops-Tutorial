# Counting the number of digits in a string


def count_number_of_digits(string: str) -> int:
  digits: str = "0123456789"
  count: int = 0  # initial value
  # Iterate through each character in 'string' to check whether the
  # character is a digit or not.
  for s in string:
    if str(s) in digits:
      count += 1

  return count


# Testing the function

print(count_number_of_digits("ssd72746382dsffsgd"))  # 8
print(count_number_of_digits("b40 jidofhjasd2"))  # 3
print(count_number_of_digits("ssd7834875hasfafd23424f32rf"))  # 14
