import subprocess

print("Creating database...")

subprocess.run(
    ["python", "database.py"]
)

print("Adding motivational quotes...")

subprocess.run(
    ["python", "seed_quotes.py"]
)

print("Adding users...")

subprocess.run(
    ["python", "seed_users.py"]
)

print("Adding birthday wishes...")

subprocess.run(
    ["python", "seed_wishes.py"]
)

print()

print("===================================")
print("BirthdayVerse Database Ready ✅")
print("===================================")