from console_gfx import ConsoleGfx
def dec_char_decode(tot_value): #dictionary for decimal input conversion into hex
    if tot_value == 10:
        return 'a'
    elif tot_value == 11:
        return 'b'
    elif tot_value == 12:
        return 'c'
    elif tot_value == 13:
        return 'd'
    elif tot_value == 14:
        return 'e'
    elif tot_value == 15:
        return 'f'
    else:
        return str(tot_value) #returns the hex equivalent of the digit
def to_hex_string(data):
    for i in range(len(data)):
        if data[i] > 9:
            data[i] += 55 #ord of A is  65 but the integers go up to 9 so you add 55 to account for the letters.
            data[i] = chr(data[i]).lower()
        data[i] = str(data[i])
    return ''.join(data) #adds the data together, no spaces

def count_runs(flat_data):
  count = 0
  runs = 1
  for i in range(1,len(flat_data)): #for each value in the range from (1, end of the data)
    if flat_data[i] == flat_data[i-1]:
        count += 1
    else:
        runs += 1
    if count > 15: #hexdecimal only goes up to 15
        runs += 1
        count = 0
  return runs

def encode_rle(flat_data):
  encode_rle = []
  counts = 1
  for j in range(1,len(flat_data)): #count length
    if flat_data[j] == flat_data[j-1]:
      counts += 1
      if counts >= 15:
        encode_rle.append(counts) #adds the counts into list encode_rle
        counts = 0
        encode_rle.append(int(flat_data[j-1])) #same thing as the prev. comment but adds the value of it
    else:
      encode_rle.append(counts)
      counts = 1
      encode_rle.append(int(flat_data[j-1]))
  if flat_data[-1] == flat_data[-2]:
    encode_rle.append(counts)
    encode_rle.append(int(flat_data[-1]))
  else:
    encode_rle.append(counts)
    encode_rle.append(int(flat_data[-1]))
  return encode_rle
  flat_data = input()
  print(encode_rle(flat_data.split(", "))) #the space in the input accounts for the , and space in the input^^

def get_decoded_length(rle_data):
  dec_len = 0      #dec_len is decoded length
  for r in range(len(rle_data)):
    if r % 2 == 0:
      dec_len += int(rle_data[r])
  return dec_len

def decode_rle(rle_data):
  encode_rle = []
  for r in range(len(rle_data)):
    if r % 2 == 0: #if it isn't 0 then that means it is an odd number, we only want to mess with the integer!!!
      encode_rle.extend([rle_data[r+1]] * rle_data[r])
  return encode_rle

def string_to_data(data_str): #data string
  raw_data = list(data_str)
  for i in range(len(raw_data)):
      if raw_data[i].isdigit(): #only true if it is a digit
          raw_data[i] = int(raw_data[i])
      else:
          raw_data[i] = ord(raw_data[i].upper()) - ord('A') + 10 #converts A-F to 10 through 15
  return raw_data #outputs the list of rle/raw data
def to_rle_string(rle_data):
    rle_string = ''
    for i in range(len(rle_data)):
        if i % 2 == 0:
            rle_string += str(rle_data[i])
        if i % 2 != 0:
            rle_string += dec_char_decode(int(rle_data[i]))  # Add ":" for every pair except the last one
            if i != len(rle_data) - 1:
                rle_string += ':'
    return rle_string
def string_to_rle(rle_data):
    global data #allows data to be used outside of this function and not produce error
    data = []
    while ":" in rle_data:
        index = rle_data.find(":")
        sub = rle_data[0:index]
        if len(sub) == 3:
            sub = dec_char_decode(int(sub[0:2]))  + sub[2:] #takes in integer
        data.extend(string_to_data(sub)) #converts each part
        rle_data = rle_data[index+1:]
    if len(rle_data) == 3:
        rle_data = dec_char_decode(int(rle_data[0:2])) + rle_data[2:]
    data.extend(string_to_data(rle_data))
    return data
def standalone(): #prints menu
    print("\nRLE Menu")
    print("--------")
    print("0. Exit","\n1. Load File","\n2. Load Test Image","\n3. Read RLE String","\n4. Read RLE Hex String", "\n5. Read Data Hex String","\n6. Display Image","\n7. Display RLE String","\n8. Display Hex RLE Data","\n9. Display Hex Flat Data","\n\nSelect a Menu Option:")
def main():
    global image, data  # Declare data globally
    True
    image = None
    data = []  # Initialize data list
    print("Welcome to the RLE image encoder!")
    print("\nDisplaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    while True:
        standalone()  # menu
        option = int(input())
        if option == 0:
            quit()
        elif option == 1:
            print("Enter name of file to load:")
            filename = input()
            image = ConsoleGfx.load_file(filename)
        elif option == 2:
            print("Test image data loaded.")
            image = ConsoleGfx.test_image
        elif option == 3:
            data = input("Enter an RLE string to be decoded:")
            data = decode_rle(string_to_rle(data))
        elif option == 4:
            data = input("Enter the hex string holding RLE data:")
            image = decode_rle(string_to_data(data))
        elif option == 5:
            data = input("Enter the hex string holding flat data:")
            image = string_to_data(data)
        elif option == 6:
            print("Displaying image...")
            if image is None:
                print('(no data)')
            else:
                ConsoleGfx.display_image(image)
        elif option == 7:
            if image is None:
                print('(no data)')
            else:
                image = to_rle_string(encode_rle(image))
                print("RLE representation:", image)
        elif option == 8:
            image = to_hex_string(encode_rle(data))
            print("RLE hex values:", image)
        elif option == 9:
            image = to_hex_string(data)
            print("Flat hex values:", image)
        else:
            print("Error! Invalid Input.")
if __name__== "__main__":
    main()

