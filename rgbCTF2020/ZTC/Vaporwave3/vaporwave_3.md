# Vaporwave 3
## Challenge Description
Hone your skills, find new strategies, get your time splits down, and maybe you can claim the new Ninja Gaiden, Wii Sports Resort Golf, or Blindfolded Punch-Out world record speedrun!

chall.zip

## Solution
The zip files contains a list of mp3 file. Inspecting the spectrogram of all the files reveal these strings:
```
3p}
jan
n1y
OHS
4f7
z_k
se0
{ah
```
If I order the corresponding mp3 files by length (hint: speedrun), then I get: janOHS{ahse0n1yz_k4f73p}. I assumed janOHS must somehow correspond to 'rgbCTF', maybe it's a Vigenere cipher?

Putting the ciphertext through a Vigenere cipher with the key "SUMMONINGSALT" (a popular speedrunner) reveals the flag: `rgbCTF{summ0n1ng_s4l73d}`

### Author
[tiraaamisu](https://github.com/Lindzy)