"""Get book data"""

import pprint
from title_to_url import search
from bookdata import BookData

def summary(search_term: str) -> dict:
    """Get information about a book"""
    b = BookData(search(search_term))
    return b.summary()

if __name__ == "__main__":
    # Nicely render the dict
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(summary(input("Book? ")))

# if you would like to have the option to export the summary as a JSON, uncomment the following code:
#
# def summary(search_term: str, fpath: str) -> dict:
#     """Get book information and export"""
#     b = BookData(search(search_term))
#     summary = b.summary(filepath=fpath)
#     return summary
# if __name__ == "__main__":
#     Nicely render the dict
#     pp = pprint.PrettyPrinter(indent=2)
#     pp.pprint(summary(input("Book? "), input("Filepath? ")))
