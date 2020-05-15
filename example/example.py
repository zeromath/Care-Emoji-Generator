import sys
import os
sys.path.append(os.getcwd() + "/../source/")

try:
    from emojiGenerator import EmojiGenerator
    from bookHandler import BookHandler
except:
    print("files not found")


if __name__ == '__main__':
    file_path = os.getcwd() + '/'
    file_name = 'output'
    file_ext = '.png'
    
    isbns = ['9781475738490', '9780024041517', '9781111569624']
    for i, isbn in enumerate(isbns):
        book_cover = BookHandler().getImageByISBN(isbn)
        EmojiGenerator().generateCareEmoji(book_cover).save(file_path + file_name + str(i) + file_ext)
