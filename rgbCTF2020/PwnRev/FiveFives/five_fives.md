# Five Fives
## Challenge Description
nc challenge.rgbsec.xyz 7425

File: main.java

## Solution
The server seeds a random number generator with the current time in ms (plus or minus 10 seconds), and then asks us to guess 5 numbers in the range 1-5 in a row, given the last 5. Each connection takes 10 seconds, and we get 20 tries on each connection. There are a couple things that look almost exploitable:
 * If we submit less than five numbers, the server will crash if they're correct. So we could (for instance) submit just "1", and then if the connection closes, we know the correct answer starts with "1", narrowing our search. Then try "1 1", "1 2", "1 3" until we get another disconnect. But this doesn't work -- because the connection is closed, and the seed is regenerated anew on each reconnect.
 * We've seen the last 5 numbers, which is 1 out of 3125 possibilities. There are 10000 possible seeds. By trying the seeds on our machine, we can narrow it to about 3 possible seeds, and replicate the future behavior. Unfortunately, Java's SecureRandom class doesn't just *set* a seed, it *mixes in* a seed, and SecureRandom starts with OS-supplied true randomness. So guessing the seed is not enough to predict the future.

So what's left? Brute force. We have a 1-in-3125 chance of getting a guess right, 20 tries per connect, 10 seconds per connect. `3125/20*10/60 = 26` minutes. Sounds good.

Solver script [here](solver.java)

### Author
[timeroot](https://github.com/timeroot)