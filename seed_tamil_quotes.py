from database import (
    create_tables,
    execute_query
)

create_tables()


quotes = [

(
"முயற்சி திருவினையாக்கும். தொடர்ந்து முயற்சி செய், வெற்றி நிச்சயம்.",
"தமிழ் பழமொழி",
"Tamil",
"Motivation"
),

(
"எண்ணிய முடிதல் வேண்டும், நல்ல எண்ணம் வாழ்க்கையை உயர்த்தும்.",
"தமிழ் கவிதை",
"Tamil",
"Life"
),

(
"விழுந்தாலும் எழுந்து நிற்பவனே உண்மையான வெற்றியாளர்.",
"தமிழ் ஊக்கம்",
"Tamil",
"Motivation"
),

(
"கனவு காணுங்கள், அதை அடைய கடினமாக உழையுங்கள்.",
"அப்துல் கலாம்",
"Tamil",
"Success"
),

(
"கற்றது கைமண் அளவு, கல்லாதது உலகளவு.",
"ஔவையார்",
"Tamil",
"Education"
),

(
"நம்பிக்கை உள்ள இடத்தில் வெற்றி இருக்கும்.",
"தமிழ் சிந்தனை",
"Tamil",
"Motivation"
),

(
"நேரத்தை மதிப்பவன் வாழ்க்கையில் உயர்வான்.",
"தமிழ் சிந்தனை",
"Tamil",
"Life"
),

(
"சிறிய முயற்சிகள் பெரிய மாற்றங்களை உருவாக்கும்.",
"தமிழ் ஊக்கம்",
"Tamil",
"Success"
),

(
"தோல்வி என்பது முடிவு அல்ல, வெற்றிக்கான முதல் படி.",
"தமிழ் கவிதை",
"Tamil",
"Motivation"
),

(
"உன்னை நீ நம்பினால் உலகம் உன்னை நம்பும்.",
"தமிழ் சிந்தனை",
"Tamil",
"Confidence"
)

]


for quote in quotes:

    execute_query(
        """
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
        """,
        quote
    )


print("Tamil quotes added successfully.")