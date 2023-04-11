def divide_int_numbers(a, b):
  if b == 0:
    raise My_exceptions.exception2
    return False
  elif type(a) == int and type(b) == int:
    return int(a/b)
  elif type(a) != int or type(b) != int:
    raise My_exceptions.exception1
  else:
    raise My_exceptions.exception3
    return False