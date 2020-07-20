# Sadistic Reversing 2
## Challenge Description
hopefully harder now
`[117, 148, 123, 5, 54, 9, 61, 234, 45, 4, 2, 40, 88, 111, 65, 65, 46, 23, 114, 110, 102, 148, 136, 123, 30, 5, 214, 231, 225, 255, 239, 138, 211, 208, 250, 232, 178, 187, 171, 242, 255, 30, 39, 19, 64, 17, 40, 29, 13, 27]`

File: sadrev

## Solution
This is a lot like Sadistic Reversing 1, but it seems that certain numbers of output depend on other ones elsewhere in the input -- but still, the first byte of output is determined by just one thing, and the second byte is determined by two, and so on. Probably some loop of the form

```
long state = 0;
for(int i=0; i<input.length; i++){
	char next = input.charAt( mystery1(i) );
	result.append( mystery2(state,next) );
	state = mystery3(state,next);
}
```

So let's blackbox this. Since we're not sure where we'll have to change a byte in input to get the right change in output, we just choose a random place and hope it improves it. [script](solver.py)

Takes about two minutes to run. (And what a shame I didn't optimize it -- we missed first blood by a matter of seconds!)

### Author
[timeroot](https://github.com/timeroot)