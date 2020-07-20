# Emoji Chain Stego
## Challenge Description
I was inspired by the incredibly intelligent and nuanced conversations in #cryptography and #forensics to create a new stego technique!

File: emoji_chain_stego.png

## Solution

The PNG shows one picture followed by 30 apparently identical emojis. PNGs have
lossless compression, so we expect the pixel data for these 30 emojis to be identical.
We divide the 30 emojis into 30 160x160 tiles. We find that the tiles are not all the same,
suggesting that the hidden information is stored in these differences somehow.

To get the unmodified emoji, we take the mode of the 30 modified tiles. We then take the
difference between the modified and modified tiles and examine the differences. The
modified tiles are very similar to the unmodified tile, except some pixels are off by one
in one of the channels. Across all tiles, the modifications occur in a 128x128 box.

Since ASCII characters take a value from 0-127, we hypothesize that the location of the
differences correspond to the characters of the flag. The flags begin with "rgb", which
corresponds to ASCII values 114, 103, 98. We observe that, within the 128x128 box, the
first tile has multiple differences in row 114, the second tile has multiple differences
in row 103, and so on. These are the last rows with more than one difference.

We continue this process to get the ASCII codes from the remaining tiles. This reveals
the flag.

[Solver script](parse.py)

## Flag
```rgbCTF{Isn't_3m0ji_St3g0_fun?}```

### Author
[keegan](https://twitter.com/inf_0_)