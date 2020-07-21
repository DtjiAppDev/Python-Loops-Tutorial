# Counting the number of elements in a list until a particular class instance is encountered


def number_of_elements_till_n_class_instance(a_list: list, n_class: str) -> int:
  count: int = 0  # initial value
  for elem in a_list:
    # Stop iterating if elem is an 'n_class" class instance
    if isinstance(elem, n_class):
      return count

    count += 1


# Testing the function


class A:
  def __init__(self, a):
    self.a: int = a


print(number_of_elements_till_n_class_instance(["434", "xxs", "d234d", "3424325", "5.18", 5, "qewfefeqwgfr"], int))  # 5
print(number_of_elements_till_n_class_instance([4, 3, 2, "s", "x", 5, 1, 7, "d"], str))  # 3
print(number_of_elements_till_n_class_instance(["55", 44, A(3), A(0), "dsfdf", 13], A))  # 2
