# Grab your jisho
## Challenge Description

 これは文字化けか？それとも暗号…?

File: grab your jisho

## Solution

We are provided with a 2MB text file with characters from the Unicode CJK blocks.
The text is not recognized by web translation services, so we conclude the flag must be found some other way. We find the following string resembling a URL:

```昒鏽霱彊://鱓攫襵.扺譸醸叏褖𠆢夳鯁曵.蕐屩形/尤甠賿䵷/_/_/_/_/_____```

It seems like individual characters correspond directly to individual A-Z letters.
For example, "昒鏽霱彊://鱓攫襵." probably decodes to "http://www." This tells us we
are dealing with some sort of substitution cipher. However, it is not one-to-one
substitution, since otherwise we would expect each of the "t"s or "w"s to match the
others. This tells us that either we are working with a many-to-one substitution cipher
or perhaps a Vigenere cipher. With so much ciphertext, we can just treat it as a
many-to-one cipher, where one decoded Latin alphabet letter can be represented by
one of many CJK characters.

We start by identifying the most frequently appearing character and all of the words
it appears in. We use a dictionary of English words and their frequency to determine
the likelihood that the CJK character is an "A," "B," "C," and so on. For example, if we
are considering the character "躄," and we see start three letter words like "躄呵芀" or
"躄亟玊" or words with apostrophes like "齃劅魂'躄," we might speculate that the character
decodes to a "T" or a "S," since words with those letters in the same position are common.

If one candidate letter is significantly more likely than all the others, we make the
substitution in the text. We repeat until we have recovered a large portion of the text.
This reveals that the plaintext is taken from the book "Myths & Legends of Japan."
We find the flag added to this text, except there are some unique characters which only
appear once in the flag and cannot be decoded using frequency analysis.

```RGBCTF讞鸞鸚鱺YOMINIKUI鸝钁厵鬱```

"Yominikui" translates to "hard to read" or "illegible," so we know we are at least on the
right track. At this point, we look at the relationship between the CJK characters and Latin
characters we've decoded already. As a sample, observe the following:

```A:一 B:儿 C:亍 Z:髗```

The number of strokes in a character appears to correspond to the letter of the alphabet.
In fact, jisho.org helpfully reports the number of strokes used to write a character.
We input the 8 remaining characters to the site and find they take 27, 30, 28, 30, 30,
28, 30, and 29 strokes respectively. Since these values are greater than 26, which
corresponds to Z, we assume that these characters decode to the ASCII characters directly following z. This way the flag has the correct format, and we can understand the remaining characters in the flag.

## Flag
```rgbctf{~|~yominikui~|~}```

### Author
[keegan](https://twitter.com/inf_0_)