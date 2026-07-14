# models.py (Part 1)

from database import (
    execute_query,
    fetch_one,
    fetch_all
)

# ==========================
# USERS
# ==========================

def create_user(
    name,
    email,
    phone,
    password,
    birthday,
    gender,
    profile_image
):

    query = """
    INSERT INTO users
    (
        name,
        email,
        phone,
        password,
        birthday,
        gender,
        profile_image
    )

    VALUES
    (
        ?,?,?,?,?,?,?
    )
    """

    execute_query(
        query,
        (
            name,
            email,
            phone,
            password,
            birthday,
            gender,
            profile_image
        )
    )


def get_all_users():

    query = """
    SELECT *
    FROM users
    ORDER BY name
    """

    return fetch_all(query)


def get_user_by_id(user_id):

    query = """
    SELECT *
    FROM users
    WHERE id=?
    """

    return fetch_one(query, (user_id,))


def get_user_by_email(email):

    query = """
    SELECT *
    FROM users
    WHERE email=?
    """

    return fetch_one(
        query,
        (email,)
    )
def update_user(
    user_id,
    name,
    phone,
    birthday,
    gender,
    profile_image
):

    query = """
    UPDATE users

    SET

    name=?,
    phone=?,
    birthday=?,
    gender=?,
    profile_image=?

    WHERE id=?
    """

    execute_query(
        query,
        (
            name,
            phone,
            birthday,
            gender,
            profile_image,
            user_id
        )
    )


def delete_user(user_id):

    query = """
    DELETE FROM users
    WHERE id=?
    """

    execute_query(query, (user_id,))
    # models.py (Part 2)

# ==========================
# BIRTHDAYS
# ==========================

def get_today_birthdays(today):

    query = """
    SELECT *
    FROM users
    WHERE strftime('%m-%d', birthday)=?
    ORDER BY name
    """

    return fetch_all(
        query,
        (today,)
    )


def get_tomorrow_birthdays(tomorrow):

    query = """
    SELECT *
    FROM users
    WHERE strftime('%m-%d', birthday)=?
    ORDER BY name
    """

    return fetch_all(
        query,
        (tomorrow,)
    )


# ==========================
# WISHES
# ==========================

def create_wish(
    sender_id,
    receiver_id,
    message,
    visible_on,
    anonymous
):

    query = """
    INSERT INTO wishes
    (
        sender_id,
        receiver_id,
        message,
        visible_on,
        anonymous
    )

    VALUES
    (
        ?,?,?,?,?
    )
    """

    execute_query(
        query,
        (
            sender_id,
            receiver_id,
            message,
            visible_on,
            anonymous
        )
    )


def get_received_wishes(receiver_id):

    query = """
    SELECT *

    FROM wishes

    WHERE receiver_id=?

    ORDER BY created_at DESC
    """

    return fetch_all(
        query,
        (receiver_id,)
    )


def get_sent_wishes(sender_id):

    query = """
    SELECT *

    FROM wishes

    WHERE sender_id=?

    ORDER BY created_at DESC
    """

    return fetch_all(
        query,
        (sender_id,)
    )


def delete_wish(wish_id):

    query = """
    DELETE FROM wishes
    WHERE id=?
    """

    execute_query(
        query,
        (wish_id,)
    )
    # models.py (Part 3)

# ==========================
# QUOTES
# ==========================

def add_quote(
    quote,
    author,
    language,
    category
):

    query = """
    INSERT INTO quotes
    (
        quote,
        author,
        language,
        category
    )

    VALUES
    (
        ?,?,?,?
    )
    """

    execute_query(
        query,
        (
            quote,
            author,
            language,
            category
        )
    )


def get_all_quotes():

    query = """
    SELECT *
    FROM quotes
    ORDER BY id DESC
    """

    return fetch_all(query)


def get_random_quote():

    query = """
    SELECT *
    FROM quotes
    ORDER BY RANDOM()
    LIMIT 1
    """

    return fetch_one(query)


def delete_quote(quote_id):

    query = """
    DELETE FROM quotes
    WHERE id=?
    """

    execute_query(
        query,
        (quote_id,)
    )


# ==========================
# NOTIFICATIONS
# ==========================

def create_notification(
    user_id,
    title,
    body
):

    query = """
    INSERT INTO notifications
    (
        user_id,
        title,
        body
    )

    VALUES
    (
        ?,?,?
    )
    """

    execute_query(
        query,
        (
            user_id,
            title,
            body
        )
    )


def get_notifications(user_id):

    query = """
    SELECT *

    FROM notifications

    WHERE user_id=?

    ORDER BY created_at DESC
    """

    return fetch_all(
        query,
        (user_id,)
    )


def mark_notification_read(notification_id):

    query = """
    UPDATE notifications

    SET is_read=1

    WHERE id=?
    """

    execute_query(
        query,
        (notification_id,)
    )


def delete_notification(notification_id):

    query = """
    DELETE FROM notifications

    WHERE id=?
    """

    execute_query(
        query,
        (notification_id,)
    )
    # models.py (Part 4 - Final)

# ==========================
# DASHBOARD
# ==========================

def total_users():

    query = """
    SELECT COUNT(*) AS total
    FROM users
    """

    row = fetch_one(query)

    return row["total"]


def total_wishes():

    query = """
    SELECT COUNT(*) AS total
    FROM wishes
    """

    row = fetch_one(query)

    return row["total"]


def total_quotes():

    query = """
    SELECT COUNT(*) AS total
    FROM quotes
    """

    row = fetch_one(query)

    return row["total"]


def total_notifications():

    query = """
    SELECT COUNT(*) AS total
    FROM notifications
    """

    row = fetch_one(query)

    return row["total"]


def dashboard_statistics():

    return {

        "total_users": total_users(),

        "total_wishes": total_wishes(),

        "total_quotes": total_quotes(),

        "total_notifications": total_notifications()

    }


# ==========================
# SEARCH
# ==========================

def search_users(keyword):

    query = """
    SELECT *

    FROM users

    WHERE name LIKE ?

       OR email LIKE ?

    ORDER BY name
    """

    keyword = f"%{keyword}%"

    return fetch_all(
        query,
        (
            keyword,
            keyword
        )
    )


# ==========================
# UPCOMING BIRTHDAYS
# ==========================

def all_birthdays():

    query = """
    SELECT *

    FROM users

    ORDER BY birthday
    """

    return fetch_all(query)