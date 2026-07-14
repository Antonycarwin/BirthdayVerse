# quote_service.py

from models import (
    get_random_quote
)


def random_quote():

    quote = get_random_quote()

    if quote:

        return {

            "quote": quote["quote"],

            "author": quote["author"],

            "language": quote["language"],

            "category": quote["category"]

        }

    return {

        "quote":
        "Believe in yourself. Every day is another opportunity to become stronger.",

        "author":
        "BirthdayVerse",

        "language":
        "English",

        "category":
        "Motivation"

    }


def tamil_quotes():

    from database import fetch_all

    return fetch_all(
        """
        SELECT *

        FROM quotes

        WHERE language='Tamil'

        ORDER BY RANDOM()
        """
    )


def english_quotes():

    from database import fetch_all

    return fetch_all(
        """
        SELECT *

        FROM quotes

        WHERE language='English'

        ORDER BY RANDOM()
        """
    )


def category_quotes(category):

    from database import fetch_all

    return fetch_all(
        """
        SELECT *

        FROM quotes

        WHERE category=?

        ORDER BY RANDOM()
        """,
        (category,)
    )