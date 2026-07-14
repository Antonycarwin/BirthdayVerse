from birthday import (
    today_birthdays,
    tomorrow_birthdays
)


def birthday_notifications():

    notifications = []


    for person in today_birthdays():

        notifications.append(
            {
                "message":
                f"🎂 Today is {person['name']}'s birthday!"
            }
        )


    for person in tomorrow_birthdays():

        notifications.append(
            {
                "message":
                f"🎁 Tomorrow is {person['name']}'s birthday!"
            }
        )


    return notifications