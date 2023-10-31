# Christopher Webb
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

def decode(encoded_password):
    # takes in the encoded password and returns the original password.
    decoded_password = ''

    for digit in encoded_password:
        # Shift the digit down by 3 numbers
        decoded_digit = str((int(digit) - 3))
        decoded_password += decoded_digit

    return decoded_password

while True:
  print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
  option = int(input("Please enter an option:"))
  if option == 1:
      password = input("Please enter your password to encode:")
      pw = encode(password)
      print("Your password has been encoded and stored!")
  if option == 2:
      print(f"The encoded password is", {pw} + ',', "and the original password is", {decode(pw)} + '.')
  if option == 3:
      quit()
