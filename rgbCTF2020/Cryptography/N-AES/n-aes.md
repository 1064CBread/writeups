# N-AES
## Challenge Description
What if I encrypt something with AES multiple times? `nc challenge.rgbsec.xyz 34567`

File: n_aes.py

## Solution
The file `n_aes.py` contains an encryption method which does repeated AES. The server
first outputs a challenge which is AES-ECB encrypted 128 times, and it also allows the
user to submit the decrypted challenge. If the decrypted challenge is correct, the
server outputs the flag.

However, there is an error in the challenge encryption procedure.

```
def rand_block(key_seed=urandom(1)):
    seed(key_seed)
    return bytes([randint(0, 255) for _ in range(BLOCK_SIZE)])
```

This function is called 128 times to generate 128 AES keys. However, the error is in
the use of `urandom(1)` as the default parameter. Instead of being called on every
invocation, `urandom` is called only once when the function is defined. Thus the
default parameter of `rand_block` can have only one of 256 possible values.

This means that there are only 256 possible sequences of 128 AES keys. We brute force
all of them to find the candidate key which decrypts the challenge properly. We send
this to the server and retrieve the flag.

## Flag
```rgbCTF{i_d0nt_7hink_7his_d03s_wh47_y0u_7hink_i7_d03s}```

### Author
[keegan](https://twitter.com/inf_0_)