from datetime import datetime, timedelta

from models import (
    get_today_birthdays,
    get_tomorrow_birthdays,
    all_birthdays
)


def today_birthdays():

    today = datetime.now().strftime("%m-%d")

    return get_today_birthdays(today)



def tomorrow_birthdays():

    tomorrow = (
        datetime.now()
        +
        timedelta(days=1)
    ).strftime("%m-%d")

    return get_tomorrow_birthdays(tomorrow)



def upcoming_birthdays():

    users = all_birthdays()

    today = datetime.today().date()

    result = []


    for user in users:

        if not user["birthday"]:

            continue


        birth_date = datetime.strptime(
            user["birthday"],
            "%Y-%m-%d"
        )


        next_birthday = birth_date.replace(
            year=today.year
        )


        if next_birthday.date() < today:

            next_birthday = next_birthday.replace(
                year=today.year + 1
            )


        days_left = (
            next_birthday.date()
            -
            today
        ).days


        time_difference = (
            next_birthday
            -
            datetime.now()
        )


        total_seconds = int(
            time_difference.total_seconds()
        )


        days = total_seconds // (24 * 3600)

        hours = (
            total_seconds % (24 * 3600)
        ) // 3600

        minutes = (
            total_seconds % 3600
        ) // 60


    result.append({

    "id": user["id"],

    "name": user["name"],

    "birthday": user["birthday"],

    "days_left": days,

    "hours_left": hours,

    "minutes_left": minutes

})

    result.sort(
        key=lambda x:x["days_left"]
    )


    return result