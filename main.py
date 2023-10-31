#This is Adriel
def encode(password):
  pw = ''
  for value in password:
      if value == '0':
          pw += '3'
      elif value == '1':
          pw += '4'
      elif value == '2':
          pw += '5'
      elif value == '3':
          pw += '6'
      elif value == '4':
          pw += '7'
      elif value == '5':
          pw += '8'
      elif value == '6':
          pw += '9'
      elif value == '7':
          pw += '0'
      elif value == '8':
          pw += '1'
      elif value == '9':
          pw += '2'
  return pw

while True:
  print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
  option = int(input("Please enter an option:"))
  if option == 1:
      password = input("Please enter your password to encode:")
      pw = encode(password)
      print("Your password has been encoded and stored!")
  if option == 2:
      print("The encoded password is", pw + ',', "and the original password is", password + '.')
  if option == 3:
      quit()