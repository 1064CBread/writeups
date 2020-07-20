# Lo-fi
## Challenge Description
File: lofi.wav

## Solution
We are given a .wav file. Listening to it, it's generally some nice simple music; around 30 seconds, it gets a little bit more random. As it ends, there's a few quick beeps that sound out of place. What are those beeps?

Opening this up in Audacity and looking at the spectrogram, we see the letters "tinyurl" spelled out by the quick beeps. This suggests that we need to find a 'shortcode', and then visit http://tinyurl.com/<that shortcode>.

The flavortext ("Don't let your dreams be ones and zeroes") suggests that we should be looking for something like binary. The somewhat irregular notes in the second half of the song (29.6s - 41.5s) are a candidate. Starting from the drop, we count with the beat, writing down a 0 for each time there is no note, and 1 for each time there is. The pitch is irrelevant.

This gives the string 011001100110101000101101001100110011000000110010. Doing this in real time was way to hard, but if we slowed the song down by 4x it was much more doable. Music training is recommended.

We have 48 bits, which is good, cause that's a multiple of 8. Decoding to ASCII gives "fj-302". http://tinyurl.com/fj-302 redirects to a Pastebin that says "rgbCTF{subscr1b3_t0_qu1nt3c_0n_yt_plz}".

### Author
[timeroot](https://github.com/timeroot)