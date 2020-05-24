import os
from PIL import Image
import PIL
from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app
from bookHandler import BookHandler
from emojiGenerator import EmojiGenerator
from werkzeug.utils import secure_filename

def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('upload_image'))

@app.route('/upload-image', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("No filename")
                return redirect(request.url)
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
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
    full_name = os.path.join('images', filename)
    return render_template("show_image.html", userfile = full_name)

@app.route('/emoji/<filename>')
def emoji(filename):
    eg = EmojiGenerator()
    img = Image.open(os.path.join(app.config['IMAGE_UPLOADS'], filename))
    ext = filename.rsplit(".", 1)[1]
    temp_filename = 'temp.png'
    temp_img = eg.generateCareEmoji(img)
    temp_img.save(os.path.join(app.config['IMAGE_UPLOADS'], temp_filename))
    return redirect(url_for('static', filename = 'images/' + temp_filename))
