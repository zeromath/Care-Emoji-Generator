import os
import uuid
from io import BytesIO
from PIL import Image
import PIL
from flask import render_template, flash, redirect, url_for, request, send_from_directory, after_this_request, send_file
from app import app
from bookHandler import BookHandler
from emojiGenerator import EmojiGenerator
from werkzeug.utils import secure_filename

def splitExtension(s):
    t = s.rsplit(".", 1)
    return (t[0], t[1])

def getRandomName(ext):
    return str(uuid.uuid4())[-12:] + '.' + ext

def allowedImage(filename):
    if not "." in filename:
        return False

    _, ext = splitExtension(filename)

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/')
@app.route('/index')
def index():
    tmp_path = os.path.join(app.config["IMAGE_UPLOADS"], app.config["IMAGE_FOLDER"])
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)
    return render_template('index.html')

def allowedISBN(s):
    return s.isnumeric() if len(s) == 13 else False

@app.route('/isbn', methods=["GET", "POST"])
def isbn():
    if request.method == "POST":
        if request.form:
            isbn = request.form['isbn']
            if allowedISBN(isbn):
                bh = BookHandler()
                filename = getRandomName('png')
                bh.getImageByISBN(isbn).save(os.path.join(app.config["IMAGE_UPLOADS"], app.config["IMAGE_FOLDER"], filename))
                return redirect(url_for('show_image', filename=filename))
            else:
                return redirect(request.url)
    return render_template('isbn.html')

@app.route('/upload-image', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                return redirect(request.url)
            if allowedImage(image.filename):
                _, ext = splitExtension(image.filename)
                filename = getRandomName(ext)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], app.config["IMAGE_FOLDER"], filename))
                return redirect(url_for('show_image', filename=filename))
            return redirect(request.url)
        else:
            print("file type not allowed")
            return redirect(request.url)
    return render_template('upload_image.html')

@app.route('/show-image/<filename>', methods = ["GET", "POST"])
def show_image(filename):
    if request.method == "POST":
        return redirect(url_for('emoji', filename=filename))
    full_name = os.path.join(app.config["IMAGE_FOLDER"], filename)
    return render_template("show_image.html", userfile = full_name)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/emoji/<filename>')
def emoji(filename):
    eg = EmojiGenerator()
    file_path = os.path.join(app.config['IMAGE_UPLOADS'], app.config["IMAGE_FOLDER"], filename)
    img = Image.open(file_path)
    try:
        os.remove(file_path)
    except Exception as error:
        app.logger.error("Error deleting file", error)
        
    t_filename, _ = splitExtension(filename)
    temp_filename = 'emoji' + t_filename + '.png'
    temp_img = eg.generateCareEmoji(img)
    return serve_pil_image(temp_img)


