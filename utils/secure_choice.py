import secrets

def secure_choice(items):
    return items[secrets.randbelow(len(items))]
