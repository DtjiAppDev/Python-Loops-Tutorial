# Calculating the Decimal product of elements in a list which will work for any types of list


from decimal import Decimal  # importing necessary library


# Checking whether a string is a number or not


def is_number(string: str) -> bool:
  try:
    Decimal(string)
    return True
  except:
    return False


def decimal_product_of_list(a_list: list) -> Decimal:
  product: Decimal = Decimal("1")  # initial value
  for elem in a_list:
    try:
      # Converting 'elem' into a string at first
      str_elem: str = str(elem)
      # Checking whether str_elem is a number or not
      if is_number(str_elem):
        # Multiply 'product' by the Decimal value of str_elem
        product *= Decimal(str_elem)
    except:
      pass  # Adding code just so that no errors are thrown

  return product


# Testing the function

print(decimal_product_of_list([4, 3, "5.17", "3.22s"]))  # 62.04
print(decimal_product_of_list(["4.132", "5435.34243254325", "3234324.321432153425", "ssd", "xwt", 5]))  # 363195780246.1620567101450060
