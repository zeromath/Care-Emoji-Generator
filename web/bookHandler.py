import PIL
import requests
from io import BytesIO
from PIL import Image

class BookHandler:
    """ 
    This is a class for handling book informations. 
      
    Attributes: 

    Methods:
        getImageByISBN: Grab the book cover image using ISBN using Google Book API.
    """
    def __init__(self):
        self.__google_book_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    def getImageByISBN(self, isbn):
        """ 
        The function gets the book cover via Google Book API

        Parameters: 
            isbn (string):  The string code of ISBN

        Returns: 
            Image:          An Image object of the cover
        """
        url = self.__google_book_url + isbn
        response = requests.get(url)
        jsonResponse = response.json()
    
        # Obtain the link to the cover of the book
        img_book = Image.open(BytesIO(requests.get(jsonResponse['items'][0]['volumeInfo']['imageLinks']['thumbnail']).content))
    
        return img_book

if __name__ == '__main__':
    # test
    bh = BookHandler()
    book_cover = bh.getImageByISBN('9781475738490')
    book_cover.save('test.png')
