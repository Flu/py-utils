import argparse
import sys
import textwrap as tw

def build_base64_dict(base64_dict):
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

def convert_binary(number):
	binary_number = str(bin(number))[2:]
	return "0"*(6-len(binary_number)) + binary_number

def main(args):
	ascii_dict = {i : chr(i) for i in range(0,128)}
	base64_dict = {}
	output_string = ""

	build_base64_dict(base64_dict)

	string_to_decode = args.message
	decode_flag = args.decode

	if len(string_to_decode) == 0:
		string_to_decode = input("Input the string to decode: ")

	if len(string_to_decode) % 4 != 0:
		print("Invalid input, can't decode string")
		exit

	string_to_decode = tw.wrap(string_to_decode, 4)

	for group in string_to_decode:
		indexes = list(map(lambda x : get_key_from_dict(x, base64_dict), group))
		binary_group = ''.join(list(map(convert_binary, indexes)))
		for ascii_char in tw.wrap(binary_group, 8):
			output_string += ascii_dict[int(ascii_char, 2)]
	print(output_string)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Utility for base64 encoded text")
	parser.add_argument("-d", "--decode", action="store_true", help="decode text")
	parser.add_argument("-m", "--message", default="", metavar="M", help="message to be encode/decoded")

	args = parser.parse_args()
	main(args)