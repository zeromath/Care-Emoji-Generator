from flask import Flask
import os

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "./app/static/"

app.config["IMAGE_FOLDER"] = "tmp"

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]

from app import routes
