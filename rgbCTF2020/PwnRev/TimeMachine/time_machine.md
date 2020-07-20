# Time Machine
## Challenge Description
Mom, I made a time machine! I forgot the password for it... nc challenge.rgbsec.xyz 13373

File: my_time_machine.elf

## Solution
The "time machine" here immediately hints a timing attack. Indeed, what does the binary do?
 * Generate a securely random password from the alphabet `ABC...XYZ`
 * Check user input against the password, one character at a time, returning as soon as it fails
 * Let the user try again, up to 250 times
 * If the user input matches, print out the flag.
 
The "one character at a time" part is what makes this vulnerable as a timing attack, as strings that match on longer prefixes take longer to check. This is over the network, so a few extra nanoseconds of checking would be totally unrecognizable, *but* the challenge server helpfully pauses for a whole second after each matching character. This makes the timing attack easy.

Solver script [here](time_machine.py)

### Author
[timeroot](https://github.com/timeroot)