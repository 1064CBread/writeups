# soda pop bop
## Challenge Description
nc challenge.rgbsec.xyz 6969

File: [spb](spb)

File: [libc-2.27.so](itvi.so)

## Solution

We are given a binary which is being run on a remote server. We begin by reverse
engineering the binary in Ghidra to identify exploitable issues. We find two.

First, in the function `get_drink`, the program asks the user to input the type of
drink from 0-3. It then ensures that the user input is less than 4. However, the
comparison is done using signed integers, so if the input is negative, the program
will accept it. It then writes this potentially negative value to an address based
on the `party` variable, so long as the specified party member is less than
`party_size`.

The second bug is in `main`. If the user specifies a party size of 0, a buffer of
size 0 is allocated, and 32 bytes are written to this buffer. Fortunately, this
involves writing 0xffffffffffffffff to offset +0x18 from this zero-length buffer.
This has the effect of overwriting the size of the top chunk of the heap, the
first step in a "House of Force" heap exploit. The House of Force exploit enables
us to move the top chunk of the heap anywhere in the process memory and overwrite
the contents with user-specified content.

Unfortunately, some mitigations are in place which make exploitation more complicated.
First, the binary is run with ASLR, so we need some way to deanonymize the layout.
Second, the binary has Full RELRO, so we will not be able to simply overwrite the GOT.
We are able to overcome these difficulties with the following steps.

1. Specify a party size of zero. This overwrites the size of the top chunk on the heap and allows us to move the heap pointer by specifying a particular song length in `choose_song`.
1. Invoke `sing_song` to get a pointer to the string "Never Gonna Give You Up," which is in the `.rodata` section. This deanonymizes the location of the main binary.
1. Invoke `choose_song` with a short song name. This sets `selected` song to a location in the heap and decreases the size of the top chunk. We are still able to exploit the heap overflow after this.
1. Invoke `sing_song` to get a pointer to the heap. This deanonymizes the location of the heap.
1. Use the known offset between the heap and the program data to perform the House of Force technique. We move the top chunk of the heap to be right before the `party` and `party_size` variables in the `.bss` section.
1. Attempt to allocate a very large buffer using `choose_song`. This allocation does not occur on the heap. Instead, it is allocated in a newly mapped section immediately before `libc.so`. Additionally, specify "cat /pwn/flag.txt;" as the song name. This will be the shellcode later.
1. Use `sing_song` to get a pointer to this section. This deanonymizes the location of `libc.so`.
1. Use `choose_song` to allocate 16 bytes. This occurs at the top chunk of the heap, which is in the `.bss` section. We specify a song name which changes `party` and `party_size` to point to the new top chunk of the heap.
1. Changing `party_size` allows us to use the first vulnerability in `get_drink`. Invoke this function to overwrite the size of the top chunk of the heap in preparation of another House of Force exploit.
1. Use the known offset between `.bss` and `libc.so` to move the top chunk of the heap to immediately before `__malloc_hook` in `libc.so`.
1. Allocate a song name to overwrite `__malloc_hook` with a pointer to `system` in `libc.so`.
1. Call `choose_song` with a specified size that equals the pointer to the shellcode string we wrote in the previous step. This will be passed as an argument to `__malloc_hook`, so our shellcode will be executed through the `system` call.
1. The result of the shellcode is the flag.


## Flag
```rgbCTF{l3ts_g31_th1s_bre@d}```

### Author
[keegan](https://twitter.com/inf_0_)