# icanhaz
## Challenge Description
can u haz a meaningful career in cybersecurity tool development? we hope so!

File: icanhaz.xyz

## Solution
Pretty straightforward nesting game. `file icanhaz.xyz` tells us it's `XZ compressed data`, so `mv icanhaz.xyz icanhaz.xz && xz -d icanhaz.xz`. The resulting file looks like

```
00000000: FD37 7A58 5A00 0004  ..:.!...
00000008: E6D6 B446 0200 2101  WO......
00000010: 1600 0000 742F E5A3  ......Vt
00000018: E22C 1D08 A85D 001E  S...y)..
```

so it's a hexdump of a file. A bit of bash magic to turn this back into the original:

```
cat icanhaz | sed -E -e 's/.*:(.*)  .*/\1/g' | xxd -r -p >icanhaz2
```

and `file icanhaz2` tells us that it's xz again:

```
mv icanhaz2 icanhaz2.xz && xz -d icanhaz2.xz
```

and we're left with an SVG now. Viewing the SVG, it appears blank. Opening up the SVG in a text editor shows many lines of the form

```
<rect x="66" y="30" width="1" height="1" fill="#fffffd"/>
```

That is, boxes that are just barely off-white, in the blue channel. So find-and-replace `#fffffd` with `#000000`, and we get a visible QR code. PAss that into [https://zxing.org/w/decode] and we get a base64 string:

```
/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AbxAN1dAA2XxNFhRNBaOJSxhV08AXoOcZxtalpXU+c+q/ppfZc1/t0z3BU/P16F9jAlXbjrzh5cXk/9vLbc+8NQJ8PNawtALEPD17f25zdggODx3xzNLY3SjGTIlX0fbqo6HFkHYkIzOjjUgJcN1KbzGRouW+G8TakjrJ4y5Pk7jv/stqRiV0ICPYxKpnZSEn0aLzQSl46j6H3BBUBhRuGgxue3TXIzw5HGMlchgNBs6SCfHU0SkX4zlSKqOWSyKrJ5JMgwC47en2kI68/tRNQYaYzvGGcWcR/iEgNYO/jHVDVLAAAAADjqmgxrEIjCAAH5AfINAADD+B/oscRn+wIAAAAABFla
```

de-b64ing that gives garbled nonsense, but it starts with `ý7zXZ��æ..` whic looks like another XZ compressed file. So run

```
echo "/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AbxAN1dAA2XxNFhRNBaOJSxhV08AXoOcZxtalpXU+c+q/ppfZc1/t0z3BU/P16F9jAlXbjrzh5cXk/9vLbc+8NQJ8PNawtALEPD17f25zdggODx3xzNLY3SjGTIlX0fbqo6HFkHYkIzOjjUgJcN1KbzGRouW+G8TakjrJ4y5Pk7jv/stqRiV0ICPYxKpnZSEn0aLzQSl46j6H3BBUBhRuGgxue3TXIzw5HGMlchgNBs6SCfHU0SkX4zlSKqOWSyKrJ5JMgwC47en2kI68/tRNQYaYzvGGcWcR/iEgNYO/jHVDVLAAAAADjqmgxrEIjCAAH5AfINAADD+B/oscRn+wIAAAAABFla" | base64 --decode | xz -d
```

and it prints(!) out

```
█████████████████████████████████
█████████████████████████████████
████ ▄▄▄▄▄ █▀▀ ███ ▀▀█ ▄▄▄▄▄ ████
████ █   █ █▄▀██▀▀▀ ▀█ █   █ ████
████ █▄▄▄█ █ ▄ █  ▄ ██ █▄▄▄█ ████
████▄▄▄▄▄▄▄█ █ ▀▄█ █▄█▄▄▄▄▄▄▄████
████ ▄▀ ▀▀▄▄▀▀█  ▀   ▀ ▄▄▀▄ ▀████
████▄█▀▄▀▀▄█ ▀▀  ▀▀▀▀▀▄▀▀█▄  ████
████▄ █▀ █▄ ██▄ █▀██▀  ▀▄▀   ████
████▄▀█▄█▄▄ ▄▀█ █ ██▄▀▀ ▀▄█▀ ████
████▄▄▄▄██▄▄▀▀ █ ▄▀▄ ▄▄▄ ▄█▀ ████
████ ▄▄▄▄▄ █▄█▀▄ ▄▀▄ █▄█ █  ▄████
████ █   █ █▀█▄▀▄▀▄█▄▄▄  █▄▄█████
████ █▄▄▄█ █▀▄██▀▀ ▀▀█ █▄█▄█▄████
████▄▄▄▄▄▄▄█▄▄█▄█▄█▄▄█▄██▄█▄▄████
█████████████████████████████████
█████████████████████████████████
```

which scans in a QR code reader to `rgbCTF{iCanHaz4N6DEVJOB}`.

### Author
[timeroot](https://github.com/timeroot)