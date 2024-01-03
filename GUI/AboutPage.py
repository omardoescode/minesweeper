import json

# Dictionary to hold the credits of each creator
credits = {
    "Omar Mohammed": "Creator 1",
    "Mohammed Waleed": "Creator 2",
    "Ahmed Youssef": "Creator 3",
    "Omar Hisham": "Creator 4"
}

# Function to display the credits
def display_credits():
    print("Credits:")
    for person, role in credits.items():
        print(f"{person}: {role}")

# Dictionary to hold the credits of each creator
credits = {
    "Omar Mohammed": "Creator 1",
    "Mohammed Waleed": "Creator 2",
    "Ahmed Youssef": "Creator 3",
    "Omar Hisham": "Creator 4"
}

# Function to display the credits
def display_credits():
    print("Credits:")
    for person, role in credits.items():
        print(f"{person}: {role}")


def store_credits(credits):
    with open('credits.json', 'w') as file:
        json.dump(credits, file)

def retrieve_credits():
    try:
        with open('credits.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def delete_credits():
    try:
        import os
        os.remove('credits.json')
        return False
    except FileNotFoundError:
        return False

def check_credits():
    try:
        with open('credits.json', 'r') as file:
            return True
    except FileNotFoundError:
        return False
