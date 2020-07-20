# Adequate Encryption Standard
## Challenge Description
I wrote my own AES! Can you break it?

hQWYogqLXUO+rePyWkNlBlaAX47/2dCeLFMLrmPKcYRLYZgFuqRC7EtwX4DRtG31XY4az+yOvJJ/pwWR0/J9gg==

File: adequate_encryption_standard.py

## Solution

The file `adequate_encryption_standard.py` contains an encryption method which resembles
AES. The encryption method contains a bug in the round function.

```
for _ in range(ROUNDS):
    block = enc_sub(block)
    block = enc_perm(block)
    block = bytearray(block)
    for i in range(len(block)):
        block[i] ^= key[idx]
```

After every round of regular AES, the cipher state is XOR-ed with a 16-byte round key.
However, in this case `key[idx]` uses the wrong loop variable, and its value does
not change over the encryption of an entire block. Thus we can brute force the possible
values for `key[idx]` for each block of the provided ciphertext.

We write the corresponding decryption method for the cipher, test block decryption via
brute force for every block, and recover the flag.

[Solution](decode.py)

## Flag
```rgbCTF{brut3_f0rc3_is_4LW4YS_th3_4nsw3r(but_with_0ptimiz4ti0ns)}```

### Author
[keegan](https://twitter.com/inf_0_)