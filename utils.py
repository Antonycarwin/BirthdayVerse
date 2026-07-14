# utils.py

import os
import uuid
from datetime import datetime


ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "gif"
}


def allowed_file(filename):

    return (
        "." in filename
        and
        filename.rsplit(
            ".",
            1
        )[1].lower() in ALLOWED_EXTENSIONS
    )


def unique_filename(filename):

    extension = filename.rsplit(
        ".",
        1
    )[1].lower()

    return (
        str(uuid.uuid4())
        +
        "."
        +
        extension
    )


def save_image(file, upload_folder):

    if file.filename == "":

        return None

    if not allowed_file(file.filename):

        return None

    if not os.path.exists(upload_folder):

        os.makedirs(upload_folder)

    filename = unique_filename(
        file.filename
    )

    path = os.path.join(
        upload_folder,
        filename
    )

    file.save(path)

    return filename


def today():

    return datetime.now().strftime(
        "%Y-%m-%d"
    )


def current_time():

    return datetime.now().strftime(
        "%H:%M:%S"
    )


def current_datetime():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def calculate_age(birthday):

    birth = datetime.strptime(
        birthday,
        "%Y-%m-%d"
    )

    today_date = datetime.today()

    age = (
        today_date.year
        -
        birth.year
    )

    if (
        today_date.month,
        today_date.day
    ) < (
        birth.month,
        birth.day
    ):

        age -= 1

    return age


def days_until_birthday(birthday):

    birth = datetime.strptime(
        birthday,
        "%Y-%m-%d"
    )

    today_date = datetime.today()

    next_birthday = birth.replace(
        year=today_date.year
    )

    if next_birthday.date() < today_date.date():

        next_birthday = next_birthday.replace(
            year=today_date.year + 1
        )

    return (
        next_birthday.date()
        -
        today_date.date()
    ).days