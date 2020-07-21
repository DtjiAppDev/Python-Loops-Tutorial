# Calculating the sum of the first n positive numbers


def calculate_sum_first_n(n: int) -> int:
  sum: int = 0  # initial value
  for i in range(1, n + 1):  # using n + 1 so that n is added to 'sum'
    sum += i

  return sum


# Testing the function


print(calculate_sum_first_n(50))  # 1275
print(calculate_sum_first_n(5))  # 15
