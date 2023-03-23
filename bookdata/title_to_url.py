"""Turn a title or search term into a usable URL"""

import re
import webbrowser
from bs4 import BeautifulSoup
import requests

def search(title: str):
    """
    Transform a search term into a book URL
    Utilizes GoodReads' search engine feature using webscraping
    
    Keyword arugments:
    title: str -- the search term
    
    Example:
      title = \"old man and the sea\"
      output = https://www.goodreads.com/book/show/2165.The_Old_Man_and_the_Sea?from_search=true&from_srp=true&qid=GUgCAMeZjU&rank=1
    """
    title.replace(' ', '+')

    # Scrapes search results from GoodReads
    data = requests.get(f"https://goodreads.com/search?utf8=✓&query={title}")

    soup = BeautifulSoup(data.content, "html.parser")
    # From GoodReads HTML
    search_results = soup.find_all("div", class_="u-anchorTarget")

    # Get the first search result
    res = str(search_results[0])

    book_id = re.search('id="[0-9]*"', res).group(0)

    # From GoodReads HTML
    index = str(soup).index(str(soup.find_all("div", id=book_id[4:-1])[0]))

    # this shit super jank
    html = str(soup)[index:index+1000]

    # get the first result
    link = html[html.index("/book/show/"):html.index("rank=1\"") + len("rank=1")]

    url = f"https://goodreads.com{link}"
    return url

if __name__ == "__main__":
    webbrowser.open(search(input("Search term? ")))
