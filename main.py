#main.py

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def mane_function(month_number):
  if type(month_number) != int:
    raise Exception('Only integers are allowed !')
    return False
  
