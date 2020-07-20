# Sadistic Reversing 1
## Challenge Description
`[114, 20, 119, 59, 104, 47, 75, 56, 81, 99, 23, 71, 56, 75, 124, 31, 65, 32, 77, 55, 103, 31, 96, 18, 76, 41, 27, 122, 29, 47, 83, 33, 78, 59, 10, 56, 15, 34, 94]`

File: sadrev

## Solution
The program takes in a string and outputs an array of the style

```
[100, 93, 12, ... ]
```

and we want to find the input that matches the given output. Opening it up in IDA, the relevant strings show this is running on the Graal SubstrateVM, a toolchain for compiling Java to native code. (This theory is bolstered by the fact that invoking the program with no argument leads to a `java.lang.ArrayIndexOutOfBoundsException`). Reversing compiled SubstrateVM doesn't sound like much fun, so can we blackbox this?

Some experimentation reveals that, like many simple ciphers (ahem, ARM2) the Nth character only depends on the input up to N. So we just try progressively longer things finding the right character by guessing at each step.

Solver script: [here](solver.py)

After a couple seconds, `Built  rgbCTF{th1s_pr0bably_w@s_d1ff1cult6362}`

### Author
[timeroot](https://github.com/timeroot)