import random
import string

def generate_secure_password():
    # Utwórz listę znaków specjalnych
    special_characters = '!@#$%^&*()_-+=<>?/[]{},.'

    # Wygeneruj losowe hasło
    password = ''.join([
        random.choice(string.ascii_uppercase),  # Wielka litera
        random.choice(string.ascii_lowercase),  # Mała litera
        random.choice(string.digits),           # Cyfra
        random.choice(special_characters),      # Znak specjalny
        ''.join(random.choices(string.ascii_letters + string.digits + special_characters, k=4))  # Losowe znaki
    ])

    # Mieszaj kolejność znaków w haśle
    password = ''.join(random.sample(password, len(password)))

    return password

# Przykładowe użycie funkcji
secure_password = generate_secure_password()
print(secure_password)
