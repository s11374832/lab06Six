def Menu():
    print("Decoding Menu","\n\n-------------","\n\n1. Decode hexadecimal")
    print("2. Decode binary","\n3. Convert binary to hexadecimal","\n4. Quit")
def hex_char_decode(dig): #this is the hex input dictionary and outputs a decimal digit
    if dig in ['A', 'a']: #dig is short for digit and is the hex input
        return 10
    elif dig in ['B', 'b']:
        return 11
    elif dig in ['C', 'c']:
        return 12
    elif dig in ['D','d']:
        return 13
    elif dig in ['E','e']:
        return 14
    elif dig in ['F','f']:
        return 15
    else:
        return int(dig)
def hex_string_decode(hex): #hex is the variable name for the input
    if hex[0:2] == '0x':
        hex = hex[2:]
    big_value = 0 #big sounds like beginning value
    hex_string = len(hex) - 1
    for dig in hex:
        big_value += hex_char_decode(dig)*16**hex_string
        hex_string -=1
    return big_value #big_value is a decimal
def binary_string_decode(bin): #bin = binary
    if bin[0:2] == '0b':
        bin = bin[2:]
    tot_value = 0   #total value = tot_value
    bin_string = len(bin) - 1
    for dig in bin:
        tot_value += int(dig) * 2**bin_string
        bin_string -=1
    return tot_value #tot_value is a decimal
def dec_char_decode(tot_value): #dictionary for decimal input conversion into hex
    if tot_value == 10:
        return 'A'
    elif tot_value == 11:
        return 'B'
    elif tot_value == 12:
        return 'C'
    elif tot_value == 13:
        return 'D'
    elif tot_value == 14:
        return 'E'
    elif tot_value == 15:
        return 'F'
    else:
        return str(tot_value) #returns the hex equivalent of the digit
def binary_to_hex(bin): #dec is decimal output
    dec = binary_string_decode(bin)
    list = [] #list to hold each quotient of dec
    while dec > 0:
        rem = dec % 16 #rem is short for remainder
        dec = dec // 16
        rem = dec_char_decode(rem)
        list.insert(0, str(rem)) #stores the remainders and converted hex digits
    string = ''
    for l in list:
        string = string + str(l) #combines the results and displays the final hex conversion
    return string
def main():
    while True:
        Menu() #prints menu
        print("\nPlease enter an option:")
        option = int(input())
        if option == 1:
            print("Please enter the numeric string to convert:")
            dig = input()
            print("Result:",hex_string_decode(dig))
        elif option == 2:
            print("Please enter the numeric string to convert:")
            dig = input()
            print("Result:", binary_string_decode(dig))
        elif option == 3:
            print("Please enter the numeric string to convert:")
            dig = input()
            print("Result", binary_to_hex(dig))
        elif option == 4:
            False
            print("Goodbye!")
            break
if __name__ == '__main__':
    main() #groups all the def functions under one section
