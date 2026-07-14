from datetime import datetime

from models import (
    create_wish,
    get_received_wishes,
    get_sent_wishes
)


def send_wish(
    sender_id,
    receiver_id,
    message,
    visible_on,
    anonymous
):

    create_wish(
        sender_id,
        receiver_id,
        message,
        visible_on,
        1 if anonymous else 0
    )

    return True


def received_wishes(user_id):

    wishes = get_received_wishes(user_id)

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    visible = []

    for wish in wishes:

        if wish["visible_on"] <= today:

            visible.append(wish)

    return visible


def sent_wishes(user_id):

    return get_sent_wishes(user_id)