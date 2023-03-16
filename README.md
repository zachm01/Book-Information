# Book-Information
Automatically download information on any book with only a title as input. 

# How to use
Run `main.py` at the command line, i.e. with `python3 bookdata/main.py`. Enter your intended book's title as you would in a search engine. A collection of data about the book will be scraped from GoodReads. Unfortunately, sometimes the `author` (and sometimes others) is not able to be fetched. This is to be fixed.

# Example
<i>In terminal</i><br>
`python3 bookdata/main.py`
```
>>> Book? in cold blood
>>> Export filepath? (Leave blank if none) icb.json

{ 'author': 'Truman Capote',
  'cover': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1424931136i/168642.jpg',
  'genres': [ 'Nonfiction',
              'True Crime',
              'Classics',
              'Crime',
              'Mystery',
              'History',
              'Thriller'],
  'page count': 343,
  'published in': '1965',
  'rating': 4.08,
  'synopsis': 'On November 15, 1959, in the small town of Holcomb, Kansas, '
              'four members of the Clutter family were savagely murdered by '
              'blasts from a shotgun held a few inches from their faces. There '
              'was no apparent motive for the crime, and there were almost no '
              'clues. As Truman Capote reconstructs the murder and the '
              'investigation that led to the capture, trial, and execution of '
              'the killers, he generates both mesmerizing suspense and '
              'astonishing empathy. In Cold Blood is a work that transcends '
              'its moment, yielding poignant insights into the nature of '
              'American violence.',
  'title': 'In Cold Blood'}
```
