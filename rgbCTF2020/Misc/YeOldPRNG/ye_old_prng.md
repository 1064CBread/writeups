# Ye Old PRNG
## Challenge Description
I found a really old prng... can you exploit it? `nc challenge.rgbsec.xyz 23456`

## Solution
We are strongly suggested that this is an "old" PRNG. Googling for old random number generation implementations mostly brings up stuff about LCGs ([https://en.wikipedia.org/wiki/Linear_congruential_generator]) and LFSRs ([https://en.wikipedia.org/wiki/Linear_feedback_shift_register]), so we're expecting one of those.

Connecting to the server, we can request numbers that are 3 to 100 digits long; it will then produce a sequence of random numbers for us. One of those first things to jump out is that each number appears to be entirely determined by the previous: in particular, when using 3 digits, "69" is always seen to generate "476", and this appears to occur rather frequently.

Moving up to 100 digits numbers, it's pretty clear that it's not an LCG. An LCG is affine, so two inpurt numbers that are "a" apart lead to k*a difference in the results; from two (input,output) pairs we can determine what k is, and then check this against a third pair. It doesn't work. It could be an LFSR but it's not clear exactly how that would translate here. An LFSR generates a stream of bits, which would need to be converted to these integers. And as we noted, there doesn't seem to be any hidden state.

Another big giveaway is that on the n=4 setting, we sometimes see loops like 4200 -> 6400 -> 9600 and so on, all ending with double zeros. There's something base-10ish going on here.

A bit more digging on PRNGs brings us to [https://en.wikipedia.org/wiki/List_of_random_number_generators], where we see that the oldest one is the "middle square" algorithm. This fits perfectly: `69*69 = 4761 -> 476`, and `4200*4200 = 17640000 -> 6400`.

We write this in Mathematica as `f[a_] := IntegerDigits[a^2, 10][[50, 150]]`, although a bit of padding comes in to play with `a^2` is not full length. We can predict numbers and we pass the server.

### Author
[timeroot](https://github.com/timeroot)