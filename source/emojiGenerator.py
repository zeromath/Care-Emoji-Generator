import PIL
from PIL import Image
from bookCover import BookHandler

class EmojiGenerator:
    def __init__(self):
        self.__img_emoji = Image.open("./images/emoji.png")
        self.__img_emoji = self.__img_emoji.convert("RGBA")

        self.__img_arm = Image.open("./images/arm.png")
        self.__img_arm = self.__img_arm.convert("RGBA")
    
    def generateCareEmoji(self, img_book, 
                                rotation_angle = -20, 
                                keep_ratio = True, 
                                img_width = 1000, 
                                img_height = 1000):
        img_emoji = self.__img_emoji.copy()
    
        img_book = img_book.convert("RGBA")

        emoji_w, emoji_h = img_emoji.size

        if keep_ratio:
            book_w, book_h = img_book.size
            new_w = 1000 * book_w // book_h
            new_h = 1000
        else:
            new_w, new_h = img_width, img_height

        img_book = img_book.resize((new_w, new_h), Image.ANTIALIAS)

        img_book = img_book.rotate(rotation_angle, expand = 1)


        fff = Image.new('RGBA', (new_w, new_h), (255,)*4)
        fff = fff.rotate(rotation_angle, expand = 1, fillcolor = (0,)*4)

        img_emoji.paste(img_book, (int(emoji_w * 0.2), int(emoji_h * 0.25)), mask = fff)


        img_emoji.paste(self.__img_arm, (0, 0), mask = self.__img_arm.split()[3])
        return img_emoji

if __name__ == '__main__':
    #isbn = '9781475738490'
    #emoji = generateBookCareEmoji(getImageByISBN(isbn))
    #emoji.save('output.png')
    
    #isbn2 = '9780024041517'
    #generateBookCareEmoji(getImageByISBN(isbn2)).save('output2.png')
    
    isbn3 = '9781111569624'
    book_cover = BookHandler().getImageByISBN(isbn3)
    EmojiGenerator().generateCareEmoji(book_cover).save('output3.png')
