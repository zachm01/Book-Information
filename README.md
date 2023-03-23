# Book-Information
Automatically download information on any book from Goodreads with only a title as input using Python.

# Doesn't Goodreads have an API?
Technically, they do. However, they no longer issue API keys and the current version of the tool is soon to be deprecated, hopefully to be replaced, but no promises have been made. Until they do that, the only thing I could think of was webscraping. This is the first main project in which I have used webscraping so this is mainly an exercise in programming for myself.

# How to use
Run `main.py` at the command line, i.e. with `python3 bookdata/main.py`. Enter your intended book's title as you would in a search engine. A collection of data about the book will be scraped from GoodReads. Unfortunately, sometimes the `author` (and sometimes others) is not able to be fetched. This is to be fixed.

# Wait why do I see Javascript here? I thought you said you were using Python!!1!1!
In the bookdata/bookdata/test directory is a Google Apps Script file (`book_data_slides.gs`) that I wrote that I use to apply the functionality of the Python script. This file creates a slides presentation from the data the Python script scraped. 

# <i>A Warning!</i>
This script does not always work. It can be quite buggy and unreliable due to (I think) the nature of webscraping so proceed with caution and please do not use this in any high-stakes context.

# Example
<i>In terminal</i>
<i>Italics</i> represent the user's input

```
users-macbook-pro: <i>python3 bookdata/main.py</i>
Book? <i>in cold blood</i>
Export filepath? (Leave blank if none) <i>icb.json</i>

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

The output is saved in `icb.json` in the directory
