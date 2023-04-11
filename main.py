#main.py

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def mane_function(month_number):
  if type(month_number) != int:
    raise Exception('Only integers are allowed !')
    return False
  elif month_number in range(1, 13):
    for number, name in enumerate(MONTHS):
      if month_number == number + 1:
        return 'It is ' + name
  elif month_number not in range(1, 13):
    raise Exception('Only integers from 1 till 12 are allowed !')
    return False
  else: 
    raise Exception('Some unexpected Exception !')
    return False
  
def test_function(num_list):

  array = []

  if num_list[0] == " ":
    raise Exception('First character must be a digit !')
    return False
  if num_list[len(num_list) - 1] == " ":
    raise Exception('Last character must be a digit !')
    return False
