# Secure RSA
## Challenge Description
We have created the securest possible RSA algorithm! (Put your flag in the flag format.)

File: srsa.txt

## Solution
We are given the following nonsense:

```
Secure RSA (SRSA) is a new, revolutionary way to encrypt your data that ensures the original message is unrecoverable by hackers. Top scientists from around the world have confirmed this mathematically irrefutable fact. 3 of our very own RGBSec members have developed this method, and we present it to you here. Granted, the method is very simple, and we aren't quite sure why nobody has thought of it before. Levying the power of uninjectivity, we set e to a small number. 0, in fact. Let's calculate the cipher now: (anything)^0 = 1. Since the message before encryption could have been any number in the world, the ciphertext is uncrackable by hackers. 

n: 69696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969696969

e: 0

c: 1
```

Well, yes, okay, there's clearly no way to undo this encryption, but the flag data has to be somewhere -- the flavortext then? We have a lot of flavortext. Looking at the first letters of each sentence:

ST3GL0LS

so the flag is `rgbCTF{ST3GL0LS}`.

### Author
[timeroot](https://github.com/timeroot)