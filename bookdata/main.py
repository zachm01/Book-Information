"""
Main file. Downloads the book data.

Functionality:
 -- Fetch the book data
 -- Prints it out nicely with PrettyPrinter
 -- Copies the data to the clipboard
"""

import pprint
from title_to_url import search
import pyperclip
from bookdata import BookData

def summary(search_term: str, fpath="") -> dict:
    """Get information about a book"""
    b = BookData(search(search_term))
    # Check if the user has specified a file path
    if fpath:
        return b.summary(filepath=fpath)
    return b.summary()

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=2)
    total_data = []
    num_books = int(input("How many books would you like? "))
    for i in range(num_books):
        info = summary(input("Book? "), input("Export filepath? (Leave blank if none) "))
        pp.pprint(info)
        total_data.append(info)

    copy = input("Copy to clipboard? ")

    if copy.lower() == "yes":
        for i, data in enumerate(total_data):
            total_data[i] = str(data).replace("'", "\"")
        print(total_data)
        pyperclip.copy(str(total_data))
