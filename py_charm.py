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

class My_exceptions(object):
  class exception1(Exception):
    def __str__(self):
      return "This is my Exception1. Only integers are allowed !"
  class exception2(ZeroDivisionError):
    def __str__(self):
      return "This is My_ZeroDivisionError. Divide by 0 is not allowed !"
  class exception3(Exception):
    def __str__(self):
      return "Some unexpected Exception !"
>>>>>>> test
