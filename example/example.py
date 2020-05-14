import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../source/")

try:
    from emojiGenerator import EmojiGenerator
    from bookCover import BookHandler
except:
    print(os.path.dirname(__file__))


if __name__ == '__main__':
    file_path = 'example/'
    file_name = 'output'
    file_ext = '.png'
    
    isbns = ['9781475738490', '9780024041517', '9781111569624']
    for i, isbn in enumerate(isbns):
        book_cover = BookHandler().getImageByISBN(isbn)
        EmojiGenerator().generateCareEmoji(book_cover).save(file_path + file_name + str(i) + file_ext)
