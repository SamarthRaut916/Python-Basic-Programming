# --------------------------------------------
# ✅ Exercise 1: Student Directory
# --------------------------------------------
students = [
    ("Ram", 20, "A"),
    ("shham", 22, "B"),
    ("Monya", 19, "A"),
]

student_dict = {}
for name, age, grade in students:
    student_dict[name] = {'age': age, 'grade': grade}

print("Exercise 1 - Student Directory:")
print(student_dict)
print()

# --------------------------------------------
# ✅ Exercise 2: Word Frequency Counter
# --------------------------------------------
import string

text = "Hello world! Hello, Python. This is a hello world program."

# Clean and split the text
cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
words = cleaned_text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Exercise 2 - Word Frequency:")
print(word_count)
print()

# --------------------------------------------
# ✅ Exercise 3: Reverse Lookup
# --------------------------------------------
users = {
    "user1": ("ram@example.com", "admin"),
    "user2": ("shama@example.com", "user"),
    "user3": ("monyaa@example.com", "user"),
}

email_to_find = "sunny@example.com"
found_user = None
for username, (email, role) in users.items():
    if email == email_to_find:
        found_user = username
        break

print("Exercise 3 - Reverse Lookup:")
print(f"Username for '{email_to_find}': {found_user}")
print()

# --------------------------------------------
# ✅ Exercise 4: Grouping Words by Length
# --------------------------------------------
words = ["apple", "bat", "banana", "cat", "dog", "elephant"]

length_groups = {}
for word in words:
    length = len(word)
    if length not in length_groups:
        length_groups[length] = []
    length_groups[length].append(word)

print("Exercise 4 - Group Words by Length:")
print(length_groups)
print()

# --------------------------------------------
# ✅ Exercise 5: Nested Dictionary Lookup
# --------------------------------------------
countries = {
    "India": ("New Delhi", {"Hindi": 80, "English": 10}),
    "Pakastan": ("Islamabad", {"Urdu": 75, "English": 15}),
    "Chaina": ("Beijing", {"Mandarin": 95, "English": 5}),
}

print("Exercise 5 - Country Info and Top Language:")
for country, (capital, languages) in countries.items():
    top_language = max(languages, key=languages.get)
    print(f"{country} - Capital: {capital} - Top Language: {top_language}")
print()

# --------------------------------------------
# ✅ Bonus: Flatten Employee List from Dictionary
# --------------------------------------------
company = {
    "Engineering": ["Rada", "Ram", "Shama"],
    "HR": ["Govind", "Hina", "Ishaan"],
    "Sales": ["Sunny", "Monya", "Ravi"],
}

all_employees = []
for dept in company.values():
    all_employees.extend(dept)

print("Bonus - Flattened Employee List:")
print(all_employees)
print()
