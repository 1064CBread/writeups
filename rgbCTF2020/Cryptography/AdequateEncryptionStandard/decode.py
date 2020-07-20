import base64
from adequate_encryption_standard import *


pbox_i = [pbox.index(i) for i in range(64)]

def dec_perm(in_bytes: bytes) -> bytes:
    num = int.from_bytes(in_bytes, 'big')
    binary = bin(num)[2:].rjust(BLOCK_SIZE * 8, '0')
    permuted = ''.join([binary[pbox_i[i]] for i in range(BLOCK_SIZE * 8)])
    out = bytes([int(permuted[i:i + 8], 2) for i in range(0, BLOCK_SIZE * 8, 8)])
    return out

def dec_sub(in_bytes: bytes) -> bytes:
    return bytes([sbox.index(b) for b in in_bytes])

def encrypt(plain: bytes, key: bytes) -> bytes:
    blocks = to_blocks(plain)
    out = bytearray()
    key = expand_key(key, len(blocks))
    for idx, block in enumerate(blocks):
        block = pad(block)
        assert len(block) == BLOCK_SIZE
        for _ in range(ROUNDS):
            block = enc_sub(block)
            block = enc_perm(block)
            block = bytearray(block)
            for i in range(len(block)):
                block[i] ^= key[idx]
        out.extend(block)
    return bytes(out)

def decrypt(cipher: bytes, key: bytes) -> bytes:
    blocks = to_blocks(cipher)
    out = bytearray()
    key = expand_key(key, len(blocks))
    for idx, block in enumerate(blocks):
        for _ in range(ROUNDS):
            block = bytearray(block)
            for i in range(len(block)):
                block[i] ^= key[idx]
            block = bytes(block)
            assert len(block) == BLOCK_SIZE
            block = dec_perm(block)
            block = dec_sub(block)
        out.extend(block)
    return bytes(out)

def decrypt_ks(cipher: bytes, keystream: bytes) -> bytes:
    blocks = to_blocks(cipher)
    out = bytearray()
    key = keystream
    for idx, block in enumerate(blocks):
        for _ in range(ROUNDS):
            block = bytearray(block)
            for i in range(len(block)):
                block[i] ^= key[idx]
            block = bytes(block)
            assert len(block) == BLOCK_SIZE
            block = dec_perm(block)
            block = dec_sub(block)
        out.extend(block)
    return bytes(out)

def score(pt):
    score = 0
    for p in pt:
        if p < 128:
            score += 1
    return score

def hack_block(ct):
    assert len(ct) == BLOCK_SIZE

    ks = b"\xe4"
    for i in range(256):
        ks = bytes(bytearray([i]))

        pt = decrypt_ks(ct, ks)
        if score(pt) == 8:
            print(hex(i), pt)

def hack(ct, i):
    blocks = to_blocks(ct)

    print(f"Block {i}")
    hack_block(ct[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE])
    print()


def main():
    ciphertext = "hQWYogqLXUO+rePyWkNlBlaAX47/2dCeLFMLrmPKcYRLYZgFuqRC7EtwX4DRtG31XY4az+yOvJJ/pwWR0/J9gg=="
    ct = base64.b64decode(ciphertext)
    hack(ct, 0)
    hack(ct, 1)
    hack(ct, 2)
    hack(ct, 3)
    hack(ct, 4)
    hack(ct, 5)
    hack(ct, 6)
    hack(ct, 7)

    ks = bytearray([0x9f, 0xc1, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01])
    print(decrypt_ks(ct, ks))



if __name__ == "__main__":
    main()
