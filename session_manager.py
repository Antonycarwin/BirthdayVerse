from flask import session


def login_user(user):

    session["logged_in"] = True
    session["user_id"] = user["id"]
    session["user_name"] = user["name"]
    session["user_email"] = user["email"]


def logout_user():

    session.clear()


def is_logged_in():

    return session.get("logged_in", False)


def current_user():

    if not is_logged_in():
        return None

    return {
        "id": session.get("user_id"),
        "name": session.get("user_name"),
        "email": session.get("user_email")
    }


def user_id():

    return session.get("user_id")


def user_name():

    return session.get("user_name")


def user_email():

    return session.get("user_email")