# RubikCBC
## Challenge Description
I implemented this really cool Rubiks CBC encryption algorithm and tested it on a document with my flag in it, but my dog ate my hard drive so I couldn't decrypt the file :(

Luckily I backed up the encrypted file. Can you recover my data?

File: rubiksCBC.zip

## Solution

The ZIP archive contains an encrypted file, an IV, a "SCRAMBLE," and an example of a
scramble applied to an input. Based on the challenge name, the file encryption is
a block cipher in CBC mode where the block cipher is based on a Rubik's cube.
There are 54 characters in the example block cipher encryption, which likely
correspond the the 54 colored squares on a Rubik's cube. The encryption "key" is
a sequence of turns on the cube to scramble the input state.

To avoid reimplementing the logic of a Rubiks cube, we found a python library which
implements Rubik's cube logic at
[https://github.com/pglass/cube](https://github.com/pglass/cube). We patched it slightly
to allow us to associate arbitrary byte values with the colored squares. We test against
the sample block encryption to make sure our algorithm is implemented correctly.

We use this to decrypt the encrypted file, and discover the decrypted content is a PDF
for "IP over Avian Carriers with Quality of Service." Inside this PDF, there's a QR code.
This QR code encodes the flag as text.

[Solution](decode.py)

## Flag
```rgbCTF{!IP_over_Avian_Carriers_with_QoS!}```

### Author
[keegan](https://twitter.com/inf_0_)