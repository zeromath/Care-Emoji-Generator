from flask import Flask
import os

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "./app/static/"

app.config["IMAGE_FOLDER"] = "tmp"

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]

from app import routes
