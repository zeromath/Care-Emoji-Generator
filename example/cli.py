import argparse
import sys
import os
from PIL import Image

sys.path.append(os.path.join(os.getcwd(), "..", "source"))


try:
    from emojiGenerator import EmojiGenerator
    from bookHandler import BookHandler
except:
    print("files not found.")


example_text = """example:

python3 cli.py cli_output.png --image gtm52.png
python3 cli.py cli_output2.png --isbn 9781475738490
"""

parser = argparse.ArgumentParser(description='Generating Emoji from an image file or the cover a book marked by ISBN.', epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('output', metavar = 'output', type = str, help = 'filename for output files')

parser.add_argument('--isbn', dest = 'isbn', help = 'isbn for the book')

parser.add_argument('--image', dest = 'image', help = 'an image to insert into emoji')

args = parser.parse_args()

file_path = os.getcwd()
if args.output.find('.') == -1:
    file_name = args.output + '.png'
else:
    file_name = args.output

if not args.isbn and not args.image:
    print("error: not images or ISBN designated")
elif args.isbn and args.image:
    print("error: two many arguments received")

if args.isbn:
    item_img = BookHandler().getImageByISBN(args.isbn)
else:
    item_img = Image.open(os.path.join(file_path, args.image))
    
    
EmojiGenerator().generateCareEmoji(item_img).save(os.path.join(file_path, file_name))
