"""Get book data"""

import pprint
from title_to_url import search
from bookdata import BookData

def summary(search_term: str) -> dict:
    """Get information about a book"""
    b = BookData(search(search_term))
    return b.summary()

if __name__ == "__main__":
    # Nicely render the JSON
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(summary(input("Book? ")))
