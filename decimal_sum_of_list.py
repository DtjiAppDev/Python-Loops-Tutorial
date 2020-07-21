# Calculating the Decimal sum of elements in a list which will work for any types of list


from decimal import Decimal  # importing necessary library


# Checking whether a string is a number or not


def is_number(string: str) -> bool:
  try:
    Decimal(string)
    return True
  except:
    return False


def decimal_sum_of_list(a_list: list) -> Decimal:
  sum: Decimal = Decimal("0")  # initial value
  for elem in a_list:
    try:
      # Converting 'elem' into a string at first
      str_elem: str = str(elem)
      # Checking whether str_elem is a number or not
      if is_number(str_elem):
        # Add 'sum' by the Decimal value of str_elem
        sum += Decimal(str_elem)
    except:
      pass  # Adding code just so that no errors are thrown

  return sum


# Testing the function

print(decimal_sum_of_list([4, 3, "5.17", "3.22s"]))  # 12.17
print(decimal_sum_of_list(["4.132", "5435.34243254325", "3234324.321432153425", "ssd", "xwt", 5]))  # 3239768.795864696675
