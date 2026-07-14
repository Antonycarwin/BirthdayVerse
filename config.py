import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "birthdayverse_secret_key"

DATABASE_NAME = "birthdayverse.db"

DATABASE_PATH = os.path.join(
    BASE_DIR,
    DATABASE_NAME
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "static",
    "uploads"
)

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "gif"
}

APP_NAME = "BirthdayVerse"

DEBUG = True