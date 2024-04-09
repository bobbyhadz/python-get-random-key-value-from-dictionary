# Get random Key and Value from a Dictionary in Python

import random

my_dict = {
    'name': 'Borislav Hadzhiev',
    'fruit': 'apple',
    'number': 5,
    'website': 'bobbyhadz.com',
    'topic': 'Python'
}


# ✅ get random key-value pair from dictionary
key, value = random.choice(list(my_dict.items()))
print(key, value)  # 👉️ name Borislav Hadzhiev

# -----------------------------------------------

# ✅ get random key from dictionary
key = random.choice(list(my_dict))
print(key)  # 👉️ topic

# -----------------------------------------------

# ✅ get random value from dictionary
value = random.choice(list(my_dict.values()))
print(value)  # 👉️ bobbyhadz.com