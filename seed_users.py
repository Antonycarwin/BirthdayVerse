# seed_users.py

from werkzeug.security import generate_password_hash

from database import (
    create_tables,
    execute_query
)

create_tables()

users = [

(
"Antony",
"antony@gmail.com",
"9876543210",
generate_password_hash("Antony@123"),
"2003-08-15",
"Male",
""
),

(
"Rahul",
"rahul@gmail.com",
"9876543211",
generate_password_hash("Rahul@123"),
"2002-07-13",
"Male",
""
),

(
"Priya",
"priya@gmail.com",
"9876543212",
generate_password_hash("Priya@123"),
"2003-12-08",
"Female",
""
),

(
"John",
"john@gmail.com",
"9876543213",
generate_password_hash("John@123"),
"2001-10-20",
"Male",
""
),

(
"Meena",
"meena@gmail.com",
"9876543214",
generate_password_hash("Meena@123"),
"2002-03-14",
"Female",
""
),

(
"Karthik",
"karthik@gmail.com",
"9876543215",
generate_password_hash("Karthik@123"),
"2000-06-11",
"Male",
""
),

(
"David",
"david@gmail.com",
"9876543216",
generate_password_hash("David@123"),
"2001-11-02",
"Male",
""
),

(
"Anitha",
"anitha@gmail.com",
"9876543217",
generate_password_hash("Anitha@123"),
"2003-04-27",
"Female",
""
)

]

for user in users:

    execute_query(
        """
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
        """,
        user
    )

print("Users inserted successfully.")