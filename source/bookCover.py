import PIL
import requests
from io import BytesIO
from PIL import Image

class BookHandler:
    def __init__(self):
        self.__google_book_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    def getImageByISBN(self, isbn):
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
    book_cover.show()
