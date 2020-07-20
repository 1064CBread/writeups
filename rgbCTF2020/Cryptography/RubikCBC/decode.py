from cube import Cube
import string

cube = Cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")

KEY = "D R2 F2 D B2 D2 R2 B2 D L2 D' R D B L2 B' L' R' B' F2 R2 D R2 B2 R2 D L2 D2 F2 R2 F' D' B2 D' B U B' L R' D'"

def normalize_key(key):
    key = key.replace("R2", "R R")
    key = key.replace("D2", "D D")
    key = key.replace("F2", "F F")
    key = key.replace("U2", "U U")
    key = key.replace("L2", "L L")
    key = key.replace("B2", "B B")
    
    key = key.replace("R'", "R R R")
    key = key.replace("D'", "D D D")
    key = key.replace("F'", "F F F")
    key = key.replace("U'", "U U U")
    key = key.replace("L'", "L L L")
    key = key.replace("B'", "B B B")
    
    return key

TURNS = {
    "R": Cube.R,
    "D": Cube.D,
    "F": Cube.F,
    "U": Cube.U,
    "L": Cube.L,
    "B": Cube.B,
}

def permute(pt, key=KEY):
    key = normalize_key(key).split()

    cube = Cube(pt)

    for turn in key:
        assert turn in TURNS
        TURNS[turn](cube)
        
    return cube.raw()

def permute_inverse(ct, key=KEY):
    key = normalize_key(key).split()

    cube = Cube(ct)

    for turn in key[::-1]:
        assert turn in TURNS
        TURNS[turn](cube)
        TURNS[turn](cube)
        TURNS[turn](cube)
        
    return cube.raw()

key = "F"

pt = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
ct = permute(pt, key)
pt2 = permute_inverse(ct, key)
#print(ct)
assert ct == "OOOOOOYYYYYRWWWOGGBBBYYRWWWOGGBBBYYRWWWOGGBBBGGGRRRRRR"
assert pt2 == pt

# Random test
def test_random():
    import random
    bs = bytearray([random.randrange(256) for _ in range(6*9)])
    pt = bs[:]

    ct = permute(pt)
    pt = permute_inverse(ct)
    assert pt == bs

test_random()

def xor(a, b):
    assert isinstance(a, bytearray)
    assert isinstance(b, bytearray)

    assert len(a) == 54
    assert len(b) == 54

    ret = bytearray([x ^ y for x, y in zip(a, b)])

    assert len(ret) == 54
    assert isinstance(ret, bytearray)
    return ret

def solve():
    IV = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuv"
    IV = bytearray(IV)

    with open("enc_", "rb") as f:
        ciphertext = f.read()

    ciphertext = bytearray(ciphertext)
    plaintext = bytearray()

    num_blocks = len(ciphertext) // 54

    for i in range(num_blocks):
        block = ciphertext[i*54:(i+1)*54]

        dec_block = permute_inverse(block)
        pt = xor(IV, dec_block)

        plaintext.extend(pt)

        IV = block[:]

    with open("dec_", "wb") as f:
        f.write(plaintext)

solve()

'''
cube.F()

r = cube.raw()
print(r)
print("OOOOOOYYYYYRWWWOGGBBBYYRWWWOGGBBBYYRWWWOGGBBBGGGRRRRRR")
'''
'''


Cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
Cube("OOOOOOYYYYYRWWWOGGBBBYYRWWWOGGBBBYYRWWWOGGBBBGGGRRRRRR")

OOO OOO OOO  YYY WWW GGG BBB  YYY WWW GGG BBB  YYY WWW GGG BBB  RRR RRR RRR
OOO OOO YYY  YYR WWW OGG BBB  YYR WWW OGG BBB  YYR WWW OGG BBB  GGG RRR RRR
'''
