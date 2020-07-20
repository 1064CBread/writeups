import hashlib

def h_md5(x):
    return hashlib.md5(x).hexdigest()
def h_sha256(x):
    return hashlib.sha256(x).hexdigest()

def log(x, s):
    print(x, h_md5(s), h_sha256(s))

for c in range(128):
    s = bytearray([c])
    log(chr(c), s)

for x in range(128):
    for y in range(128):
        s = bytearray([x, y])
        log(chr(x) + chr(y), s)
