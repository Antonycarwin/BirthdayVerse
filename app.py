from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from database import create_tables
from models import (
    get_user_by_email
)

from auth import (
    register_user,
    login_user
)

from birthday import (
    today_birthdays,
    tomorrow_birthdays
)

from session_manager import (
    login_user as create_session,
    logout_user,
    is_logged_in,
    current_user
)

from quote_service import (
    get_random_quote
)

app = Flask(__name__)

app.secret_key = "birthdayverse_secret_key"

create_tables()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        from utils import save_image


        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")


        if password != confirm_password:

            flash(
                "Passwords do not match.",
                "danger"
            )

            return redirect(
                url_for("register")
            )


        image = request.files.get(
            "profile_image"
        )


        profile_image = ""


        if image:

            profile_image = save_image(
                image,
                "static/uploads"
            )


        success, message = register_user(
            name,
            email,
            phone,
            password,
            birthday,
            gender,
            profile_image
        )


        if success:

            flash(
                message,
                "success"
            )

            return redirect(
                url_for("login")
            )


        flash(
            message,
            "danger"
        )


    return render_template(
        "register.html"
    )
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        success, user = login_user(
            email,
            password
        )

        if success:

            create_session(user)

            flash(
                "Login Successful.",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Invalid Email or Password.",
            "danger"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "login.html"
    )
@app.route("/dashboard")
def dashboard():

    if not is_logged_in():

        flash(
            "Please login first.",
            "warning"
        )

        return redirect(
            url_for("login")
        )


    user = current_user()


    quote = get_random_quote()


    if quote is None:

        motivational_quote = (
            "Believe in yourself. Every day is another opportunity to become stronger."
        )

    else:

        motivational_quote = quote["quote"]



    from birthday import upcoming_birthdays

    from notification_service import birthday_notifications


    notifications = birthday_notifications()


    return render_template(
        "dashboard.html",
        user=user,
        today_birthdays=today_birthdays(),
        tomorrow_birthdays=tomorrow_birthdays(),
        upcoming_birthdays=upcoming_birthdays(),
        motivational_quote=motivational_quote,
        notifications=notifications
    )
@app.route("/profile")
def profile():

    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    user = current_user()

    database_user = get_user_by_email(
        user["email"]
    )

    return render_template(
        "profile.html",
        user=database_user
    )


@app.route("/logout")
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("home")
    )


@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


@app.route("/wishes", methods=["GET", "POST"])
def wishes():

    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    from wishes import (
        send_wish,
        received_wishes
    )

    from models import (
        get_all_users
    )

    user = current_user()

    users = get_all_users()

    users = [
        u for u in users
        if u["id"] != user["id"]
    ]


    if request.method == "POST":

        receiver_id = request.form.get(
            "receiver"
        )

        message = request.form.get(
            "message"
        )

        visible_on = request.form.get(
            "visible_on"
        )

        anonymous = request.form.get(
            "anonymous"
        )


        send_wish(
            user["id"],
            receiver_id,
            message,
            visible_on,
            anonymous
        )


        flash(
            "Birthday wish sent successfully.",
            "success"
        )


        return redirect(
            url_for("wishes")
        )


    return render_template(
        "wishes.html",
        users=users,
        wishes=received_wishes(user["id"])
    )
@app.route("/admin", methods=["GET", "POST"])
def admin():

    if not is_logged_in():

        return redirect(
            url_for("login")
        )


    from models import get_user_by_id


    user = get_user_by_id(
        current_user()["id"]
    )


    if user["role"] != "admin":

        flash(
            "Access denied. Admin only.",
            "danger"
        )

        return redirect(
            url_for("dashboard")
        )


    from admin import (
        statistics,
        users,
        add_motivation_quote
    )


    if request.method == "POST":

        quote = request.form.get(
            "quote"
        )

        author = request.form.get(
            "author"
        )

        language = request.form.get(
            "language"
        )

        category = request.form.get(
            "category"
        )


        add_motivation_quote(
            quote,
            author,
            language,
            category
        )


        flash(
            "Quote added successfully.",
            "success"
        )


        return redirect(
            url_for("admin")
        )


    stats = statistics()

    user_list = users()


    return render_template(
        "admin.html",
        stats=stats,
        users=user_list
    )
@app.route("/upcoming")
def upcoming():

    if not is_logged_in():

        return redirect(
            url_for("login")
        )


    from birthday import upcoming_birthdays


    birthdays = upcoming_birthdays()


    return render_template(
        "upcoming.html",
        birthdays=birthdays
    )
@app.route("/admin/delete-user/<int:user_id>")
def delete_user(user_id):

    if not is_logged_in():

        return redirect(
            url_for("login")
        )


    from models import delete_user as remove_user


    remove_user(user_id)


    flash(
        "User deleted successfully.",
        "success"
    )


    return redirect(
        url_for("admin")
    )
if __name__ == "__main__":

    app.run(
        debug=True
    )