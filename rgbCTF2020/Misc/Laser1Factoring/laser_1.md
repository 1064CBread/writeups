# Laser 1 - Factoring
## Challenge Description
https://github.com/Quintec/LaserLang

Do you like lasers? I like lasers! Here's a warmup: create a program that factors the one number given as input. Output factors on one line in ascending order (or just leave them on the stack, as Laser has implicit output)

Example

Input: 42

Output: 1 2 3 6 7 14 21 42

Connect with `nc challenge.rgbsec.xyz 52737`

## Solution
The basic approach for LaserLang here is to
 * Figure out a "normal" assembly implementation, using reads/writes/adds/branches/gotos
 * Write all the code in one line
 * Implement the branches and gotos by leaving the line to skip around.

To avoid the headache of juggling the order of a stack, we use a separate stack for each conceptual "register" (including "array registers").

One nice thing about keeping your Laser program in one line like this, is that you can write all your documentation below it in the same file -- a unique way to comment! So my English description of the code was actually just below the program, in my .lsr file. It was as follows:

```
I  rsUD>rsUs rsU %⌝      > D(r'1'×'0'l ⌝ UU #
                  \pDrsUs/
       \                             Dp/

print "1"
store N to stack 0
store 2 to stack 1

main loop:
 duplicate N
 move N to stack 1
 move N to stack 2
 duplicate x
 move x to stack 2
 modulo
 if 0:
  copy x to stack 2
 
 decrement x (on stack 1)
 duplicate x
 duplicate x
 multiply (compute x2)
 duplicate N
 move N to stack 1
 check greater than

contine loop if 0

return
```

"N" is the number we're supposed to factor. It lives in stack 0. "x" is the number we're going to try dividing by, and we start with x = N. It lives in stack 1. We repeatedly make a copy of N and x, and divide and compute the remainder. If the remainder is 0, we copy x to stack 2 (our "results" stack). We decrement x, and continue our main loop only if x is still positive. At the end we return stack 2.

### Author
[timeroot](https://github.com/timeroot)