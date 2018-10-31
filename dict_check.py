import argparse

def wrapWords(string):
    if string == None:
        return None
    output_list = []
    word_buffer = ""
    for letter in string:
        if letter == '\n' and word_buffer != "":
            output_list.append(word_buffer)
            word_buffer = ""
        else:
            word_buffer += letter
    return output_list
        
def main(args):
    dictionary_string = ""
    with open("dictionary.txt", "r") as dict_file:
        dictionary_string = dict_file.read()
    dictionary_list = wrapWords(dictionary_string)
    if dictionary_list == None:
        print("Nothing could be extracted from the file")
    for word in dictionary_list:
        if len(word) > 15:
            print(word)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Checking whether a dictionary actually contains words")
    parser.add_argument("-f", "--file", default="", metavar="M", help="dictionary file")
    args = parser.parse_args()
    main(args)
