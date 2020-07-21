# Counting the number of positive integers needed for the sum to reach or surpass a particular value


def positive_integers_needed(sum: int) -> int:
  curr_sum: int = 0  # initial value
  n: int = 1  # initial value
  # Add 'n' to 'curr_sum' while 'curr_sum' is below 'sum'
  while curr_sum < sum:
    curr_sum += n
    n += 1

  return n - 1


# Testing the function


print(positive_integers_needed(1000))  # 45
print(positive_integers_needed(14))  # 5
print(positive_integers_needed(16))  # 6
