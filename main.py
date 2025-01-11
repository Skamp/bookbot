import sys
from getopt import getopt

################################
# Functions
################################
def countWords(string):
    return len(file_contents.split())

def charsDictionary(string):

    total_chars = {}

    for char in string:
        char = char.lower()
        if char in total_chars:
            total_chars[char] += 1
        else:
            total_chars[char] = 1
    return total_chars

def generateCharReport(string):

    charsList = []
    charsDict = charsDictionary(string)

    for char in charsDict:
        #print(f"-{char} - {charsDict[char]}")

        dict = {}
        dict["char"] = char
        dict["count"] = charsDict[char]
        charsList.append(dict)
    
    #Sort list by count
    charsList.sort(reverse=True, key=sort_on)

    for dictionary in charsList:
        if dictionary['char'].isalpha():
            print(f"The '{dictionary['char']}' character was found {dictionary['count']} times")
        
def generateReport(string):

    ################################
    # Count book words
    ################################
    total_words = countWords(string)

    print("--- Begin report of {path_to_file} ---")
    print(f"{total_words} words found in the document")
    generateCharReport(string)
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

################################
# Review parameters
################################
opts, args = getopt(sys.argv[1:],'p:',['path='])

for option, argument in opts:
    if option == '-p':
        path_to_file = argument

################################
# Read book file
################################
with open(path_to_file) as f:
    file_contents = f.read()

################################
# Generate report
################################
generateReport(file_contents)