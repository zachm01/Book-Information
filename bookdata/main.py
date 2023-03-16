"""Get book data"""

import pprint
from title_to_url import search
from bookdata import BookData

def summary(search_term: str, fpath="") -> dict:
    """Get information about a book"""
    b = BookData(search(search_term))
    if fpath:
        return b.summary()
    else:
        return b.summary(filepath=fpath)

if __name__ == "__main__":
    # Nicely render the dict
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(summary(input("Book? "), input("Export filepath? (Leave blank if none) ")))
