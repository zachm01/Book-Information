"""
Retrieve data and statistics about books from Goodreads using web scraping.

Since the Goodreads API is soon to be deprecated and no longer offers API keys,
this module uses web scraping

The following attributes need to be scraped from the website:
 -- title
 -- author
 -- average rating (out of 5)
 -- synopsis
 -- year of publication
 -- genre/genres
 -- page count
 -- url to cover image

then package the data in a JSON file
"""

import json
import re
import requests
from bs4 import BeautifulSoup
from PIL import Image

class BookData():
    """
    Get data about books from GoodReads using web scraping

    Available methods:
     -- ``get_title()``: returns a book\'s title
     -- ``get_author()``: returns a book\'s author
     -- ``get_synopsis(): returns a plot summary of the book
     -- ``get_rating()``: returns a book\'s average reader rating
     -- ``get_genres()``: returns a list of the genres this book has ben labeled as
     -- ``get_year()``: returns the year the book was published
     -- ``get_page_ct()``: returns the page count of the book
     -- ``get_image()``: returns a URL where an image of the cover of the book can
                     be found
     -- ``download_cover()``: downloads the image from the URL retrieved from 
                          get_image()
     -- ``summary()``: returns a dict with the values of all the above methods, 
                   excluding download_cover() - user can choose to export to a
                   .JSON file or not
    """
    def __init__(self, book_url: str):
        self.url = book_url
        try:
            # Get all the data from the page
            self.page = requests.get(self.url, timeout=10)
            # Parse the page content
            self.soup = BeautifulSoup(self.page.content, "html.parser")
            print("200 Connection successful")
        except Exception as exc:
            raise ConnectionError("Could not connect to webpage") from exc

    @classmethod
    def remove_html_tags(cls, input_str: str):
        """Remove HTML tages from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', input_str)

    def get_title(self):
        """Get the title of a book"""
        try:
            title = str(self.soup.find_all("h1", class_="Text Text__title1"))
            tag = "data-testid=\"bookTitle\">"
            return title[title.index(tag)+len(tag):title.index("</h1>")].replace("&amp;", "&")
        except:
            print("Could not fetch book title")
            return "title"

    def get_rating(self):
        """Get the rating of a book"""
        try:
            rating = str(self.soup.find_all("div", class_="RatingStatistics__rating"))
            return float(rating[rating.index('">')+2:rating.index("</div>")])
        except:
            print("Could not fetch average book rating")
            return "rating"

    def get_author(self):
        """Get the author of a book"""
        try:
            author = str(self.soup.find_all("h3", class_="Text Text__title3 Text__regular"))
            return author[author.index("By: ")+4:author.index("class")-2].replace("&amp;", "&")
        except:
            print("Could not fetch book author")
            return "author"

    def get_synopsis(self):
        """Get a summary of a book"""
        try:
            summary = str(self.soup.find_all("div",
                                        class_="DetailsLayoutRightParagraph__widthConstrained"))
            summary = summary[summary.index("Formatted\">")+11:summary.index("</span></div>")]
            summary = self.remove_html_tags(summary.replace("<br/><br/>", "")).replace("&amp;", "&")

            # Used to remove Librarian Notes
            cbfh = "can be found here"

            if cbfh in summary:
                return summary[summary.index(cbfh): + len(cbfh):]
            return summary.replace("'", "\'")
        except:
            print("Could not fetch book summary")
            return "synopsis"

    def get_genres(self):
        """Get the genres of a book"""
        try:
            genres = [str(i) for i in self.soup.find_all("span",
                                                    class_="BookPageMetadataSection__genreButton")]
            for i, genre in enumerate(genres):
                label_tag = "Button__labelItem\">"
                genres[i] = genre[genre.index(label_tag)+len(label_tag):]
            return [i.replace("</span></a></span>", "") for i in genres]
        except:
            print("Could not fetch book genres")
            return "genres"

    def get_year(self):
        """Get the publication info of a book"""
        try:
            info = str(self.soup.find_all("div", class_="FeaturedDetails"))
            return info[info.index("First"):info.index("</p></div>")][-4:]
        except:
            print("Could not fetch book year")
            return "year"

    def get_page_ct(self):
        """Get the page count of a book"""
        try:
            info = str(self.soup.find_all("div", class_="FeaturedDetails"))
            id_str = "pagesFormat\">"
            return int(info[info.index(id_str)+len(id_str):info.index("pages, ")-1])
        except:
            print("Could not fetch book page count")
            return "page count"

    def get_image(self):
        """Get URL of an image of the cover of a book"""
        try:
            url = str(self.soup.find_all("img", class_="ResponsiveImage"))
            return url[url.index("src=\"htt")+5:url.index(".jpg\"/>]")] + ".jpg"
        except:
            print("Could not fetch book cover")
            return "image url"

    def download_cover(self, filepath="cover.jpg"):
        """Download an image of the cover of a book"""
        try:
            url = self.get_image()
            data = requests.get(url, timeout=120).content
            try:
                with open(filepath, "wb") as f:
                    f.write(data)
                    f.close()
            except OSError:
                print("Failed to write file")
            except:
                print("Error occured when writing cover data file")

            img = Image.open('cover.jpg')
            img.show()

        except:
            print("Failed to download cover")

    def summary(self, filepath=""):
        """
        Get all of the information needed about a book
        
        Keyword arguments:
        filepath: string -- filepath to export to (.json)
        """
        information = {
            "title": self.get_title(),
            "author": self.get_author(),
            "synopsis": self.get_synopsis(),
            "rating": self.get_rating(),
            "genres": self.get_genres(),
            "published in": self.get_year(),
            "page count": self.get_page_ct(),
            "cover": self.get_image()
        }
        if filepath:
            try:
                if ".json" not in filepath.lower():
                    filepath += ".json"
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(information, f)
            except OSError:
                print("Failed to write to JSON file")
        return information
