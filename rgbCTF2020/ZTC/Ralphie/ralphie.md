# Ralphie!
## Challenge Description
Ralphie, on the double! Little Orphan Annie sent you this decoder ring, decode the secret message!

File: ralphie.png

## Solution
We're given an image of a "decoder ring" of yore -- but looking more closely, in the top left, is a QR code, with a variety of colors. Presumably we want something with just one color. So open it up in GIMP and play with the levels: go to "Curves", and give the red channel a curve that is flat at 0 until the very very end. We're left with a nice cyan QR code. Drop it in [https://zxing.org/w/decode.jspx] and we get a flag, `rgbCTF{BESURETODRINKYOUROVALTINE}`.

### Author
[timeroot](https://github.com/timeroot)