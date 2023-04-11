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
