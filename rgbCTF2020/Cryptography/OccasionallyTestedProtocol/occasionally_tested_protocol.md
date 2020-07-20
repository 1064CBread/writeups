# Occasionally Tested Protocol
## Challenge Description
But clearly not tested enough... can you get the flag?

`nc challenge.rgbsec.xyz 12345`

File: otp.py

## Solution
The file `otp.py` contains a very simple encryption method that takes the
flag, generates a keystream from a PRNG, and XORs the two together. It then
prints the encrypted flag to a network socket. If the keystream is known, then
the flag can be recovered from the ciphertext. We only need to get the correct
PRNG seed, since the keystream is generated deterministically from that.

The PRNG is seeded with the current time in seconds. Thus we get the encrypted
output from the service and brute force the exact time in seconds when the
keystream was generated. This gives the flag.

## Flag
```rgbCTF{random_is_not_secure}```

### Author
[keegan](https://twitter.com/inf_0_)
