from werkzeug.security import generate_password_hash, check_password_hash

from models import (
    create_user,
    get_user_by_email
)


def register_user(
    name,
    email,
    phone,
    password,
    birthday,
    gender,
    profile_image
):

    user = get_user_by_email(email)

    if user:

        return False, "Email already exists."

    hashed_password = generate_password_hash(password)

    create_user(
        name,
        email,
        phone,
        hashed_password,
        birthday,
        gender,
        profile_image
    )

    return True, "Registration Successful."


def login_user(email, password):

    user = get_user_by_email(email)

    if not user:

        return False, None

    if check_password_hash(
        user["password"],
        password
    ):

        return True, user

    return False, None


def change_password(
    email,
    old_password,
    new_password
):

    user = get_user_by_email(email)

    if not user:

        return False

    if not check_password_hash(
        user["password"],
        old_password
    ):

        return False

    from database import execute_query

    execute_query(
        """
        UPDATE users

        SET password=?

        WHERE email=?
        """,
        (
            generate_password_hash(new_password),
            email
        )
    )

    return True