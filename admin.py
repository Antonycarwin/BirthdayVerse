from models import (
    get_all_users,
    dashboard_statistics,
    add_quote
)

from database import execute_query


def statistics():

    return dashboard_statistics()



def users():

    return get_all_users()



def delete_user(user_id):

    execute_query(
        """
        DELETE FROM users
        WHERE id=?
        """,
        (user_id,)
    )



def add_motivation_quote(
    quote,
    author,
    language,
    category
):

    add_quote(
        quote,
        author,
        language,
        category
    )



def delete_quote(quote_id):

    execute_query(
        """
        DELETE FROM quotes
        WHERE id=?
        """,
        (quote_id,)
    )