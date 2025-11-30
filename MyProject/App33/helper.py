import hashlib, random, string

def salt(length:int=16) -> str :
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for _ in range(length))

def dk(password:str, salt:str) -> str :
    # https://datatracker.ietf.org/doc/html/rfc2898#section-5.2
    return (hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),   # хешування працює з бінарними даними       
        salt.encode("utf-8"),       # необхідне перетворення рядків
        1000000,                    # к-сть ітерацій - для збільшення "ціни" розрахунку
        16)                         # довжина - к-сть байт, що повертаються
        .hex()                      # представлення у base16 (hexadecimal)
    )