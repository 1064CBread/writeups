nc_outp = '''
Here's 10 numbers for you: 
7606
4457
3947
1064
3731
7297
365
2995
8978
1766
Here's another number I found:  24198004671426095959013618343823212179350833674108804722075704313724
'''


from random import seed, randint as w
from time import time

TARGETS = [
    532,
    9117,
    4390,
    7977,
    7961,
    5108,
    2311,
    387,
    3391,
    9683,
]

TARGETS = [
    7606,
    4457,
    3947,
    1064,
    3731,
    7297,
    365,
    2995,
    8978,
    1766,
]

#seed = int(time())
#print(seed)

def try_seed(s):
    seed(s)

    for i in range(len(TARGETS)):
        t = TARGETS[i]
        guess = w(5, 10000)

        if t != guess:
            return False
    return True

def brute_force(s0):
    s = s0 + 100
    while s > s0 - 100000:
        success = try_seed(s)
        if success:
            print("Successful seed", s)
            return s
        s -= 1

# 2020/07/12
start_seed = 1594512000
succ_seed = brute_force(start_seed)


s = succ_seed

seed(s)
print(f"Here's 10 numbers for you: ")
for _ in range(10):
    print(w(5, 10000))
    
b = bytearray([w(0, 255) for _ in range(40)])

n = 24198004671426095959013618343823212179350833674108804722075704313724

bs = n.to_bytes(28, byteorder='little')
import binascii
print(binascii.hexlify(bs))

p = bytearray([l ^ p for l, p in zip(bs, b)])
print(p)

