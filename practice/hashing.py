from hashlib import sha256


def find_hash_from_nonce(nonce):

    h = sha256(nonce.to_bytes(16)).hexdigest()
    while not h.startswith('00000'):
        nonce += 1
        h = sha256(nonce.to_bytes(16)).hexdigest()
    print(h)


find_hash_from_nonce(1)
