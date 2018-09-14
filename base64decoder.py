import sys
import textwrap as tw

ascii_dict = {chr(i) : i for i in range(0,128)}
base64_dict = {}
output_string = ""

def build_base64_dict():
	for i in range(0, 63):
		if i in range(0, 26):
			base64_dict[i] = chr(i+65)
		elif i in range(26, 52):
			base64_dict[i] = chr(i - 26 + 97)
		elif i in range(52, 62):
			base64_dict[i] = chr(i - 52 + 48)
	base64_dict[62] = "+"
	base64_dict[63] = "/"

def get_key_from_dict(search_value, dict):
	for key, value in dict.items():
		if value == search_value:
			return key
	return None

build_base64_dict()
print(base64_dict)

string_to_decode = ""
if len(sys.argv) == 1:
	string_to_decode = input("Input the string to decode: ")
else:
	string_to_decode = str(sys.argv[1])
if len(string_to_decode) % 4 != 0:
	print("Invalid input, can't decode string")
	exit
string_to_decode = tw.wrap(string_to_decode, 4)

for group in string_to_decode:
	char = ''.join(list(map(lambda x : str(bin(ascii_dict[group[0]]))[2:], group)))
	letters = tw.wrap(char, 3)
	for number in letters:
		output_string += get_key_from_dict(int(number, 2), ascii_dict)
print(output_string)