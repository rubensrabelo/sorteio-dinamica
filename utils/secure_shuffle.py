import secrets


def secure_shuffle(items):
   return sorted(items, key=lambda x: secrets.randbelow(10**12))
