import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open('top-10000-passwords.txt') as f:
        passwords = [line.rstrip() for line in f]
    with open('known-salts.txt') as f:
        salts = [line.rstrip() for line in f] if use_salts else ['']
    
    for password in passwords:
        for salt in salts:
            if hashlib.sha1(bytes(salt + password, 'utf-8')).hexdigest() == hash or hashlib.sha1(bytes(password + salt, 'utf-8')).hexdigest() == hash:
                return password
    
    return 'PASSWORD NOT IN DATABASE'
