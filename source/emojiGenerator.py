import PIL
import requests
from io import BytesIO
from PIL import Image


def getImageByISBN(isbn):
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn
    response = requests.get(url)
    jsonResponse = response.json()
    
    # Obtain the link to the cover of the book
    img_book = Image.open(BytesIO(requests.get(jsonResponse['items'][0]['volumeInfo']['imageLinks']['thumbnail']).content))
    
    return img_book

def generateBookCareEmoji(img_book):
    img_emoji = Image.open("emoji.png")
    img_emoji = img_emoji.convert("RGBA")
    
    img_arm = Image.open("arm.png")
    img_arm = img_arm.convert("RGBA")

    img_book = img_book.convert("RGBA")

    emoji_w, emoji_h = img_emoji.size
    book_w, book_h = img_book.size


    new_w = 1000 * book_w // book_h
    new_h = 1000


    rotation_angle = -20

    img_book = img_book.resize((new_w, new_h), Image.ANTIALIAS)

    img_book = img_book.rotate(rotation_angle, expand = 1)


    fff = Image.new('RGBA', (new_w, new_h), (255,)*4)
    fff = fff.rotate(rotation_angle, expand = 1, fillcolor = (0,)*4)

    img_emoji.paste(img_book, (int(emoji_w * 0.2), int(emoji_h * 0.25)), mask = fff)


    img_emoji.paste(img_arm, (0, 0), mask = img_arm.split()[3])
    return img_emoji

if __name__ == '__main__':
    #isbn = '9781475738490'
    #emoji = generateBookCareEmoji(getImageByISBN(isbn))
    #emoji.save('output.png')
    
    #isbn2 = '9780024041517'
    #generateBookCareEmoji(getImageByISBN(isbn2)).save('output2.png')
    
    #img_book = Image.open("book.png")
    #img_book = img_book.convert("RGBA")
    #generateBookCareEmoji(img_book).save('output3.png')
    
    isbn4 = '9781111569624'
    generateBookCareEmoji(getImageByISBN(isbn4)).save('output4.png')
