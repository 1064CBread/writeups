# Vaporwave 1
## Challenge Description
Do you believe in synesthesia?

File: vaporwave1.mp3

## Solution

"Synesthesia" strongly hints that the flag was hidden in visual form in the
audio file, so I loaded it in Audacity. There were two parts of the
audio—around 00:50 and 2:50, respectively—where the audio sounded distorted, so
I tried to overlay them in Gimp with a variety of layer modes to see if there
was some message hidden in the difference. This was a red herring.

Then I loaded it in [Sonic Visualizer](https://www.sonicvisualiser.org/). The
flag was readily visible in the spectrogram. I'd missed it in Audacity because
the default frequency range that Audacity displays in the spectrogram is lower
than where the flag was.

## Flag

`rgbCTF{s331ng_s0undz}`

### Author
[DeepToaster](https://github.com/deeptoaster)