# seed_wishes.py

from database import (
    create_tables,
    execute_query
)

create_tables()

wishes = [

(
2,
1,
"Happy Birthday Antony! Wishing you happiness, success and good health.",
"2026-08-15",
0
),

(
3,
1,
"May all your dreams come true. Happy Birthday!",
"2026-08-15",
1
),

(
4,
1,
"Stay strong, stay focused and keep smiling. Happy Birthday!",
"2026-08-15",
0
),

(
5,
2,
"Happy Birthday Rahul. Have a fantastic year ahead.",
"2026-07-13",
0
),

(
1,
3,
"Wishing you endless happiness and success.",
"2026-12-08",
0
),

(
6,
1,
"You inspire everyone around you. Happy Birthday!",
"2026-08-15",
1
),

(
7,
4,
"Have a wonderful birthday filled with joy.",
"2026-10-20",
0
),

(
8,
5,
"Best wishes for a successful future.",
"2026-03-14",
0
)

]

for wish in wishes:

    execute_query(
        """
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
        """,
        wish
    )

print("Birthday wishes inserted successfully.")