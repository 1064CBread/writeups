# I Love Rainbows
## Challenge Description

Can you figure out why?

File: rainbows.txt

## Solution

The file `rainbows.txt` contains 23 hashes of varying length. The lengths are consistent
with MD5 hashes and SHA256 hashes. Googling the first hash in the file shows that
`4b43b0...` is the MD5 hash of the single character "r." The name of the challenge refers
to rainbow tables, so we can create a lookup table of single-character hashes to decode
the challenge file.

We write a small script to generate the hashes of single characters, but not all of the
hashes in the challenge appear in the output. We further generate the hashes of all
printable two-character strings, and crack the remaining hashes.

Putting all the single-character and two-character hash inputs together reveals the flag.

## Flag
```rgbCTF{4lw4ys_us3_s4lt_wh3n_h4shing}```

### Author
[keegan](https://twitter.com/inf_0_)