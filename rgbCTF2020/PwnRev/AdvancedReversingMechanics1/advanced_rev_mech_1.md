# Advanced Reversing Mechanics 1
## Challenge Description
Very very advanced trust me
`71, 66, 61, 42, 53, 45, 7A, 40, 51, 4C, 5E, 30, 79, 5E, 31, 5E, 64, 59, 5E, 38, 61, 36, 65, 37, 63, 7C,`

File: arm_easy.o

## Solution
As the name ("ARM1") suggests, this is an ARM binary. It's also 32-bit, so make sure to open it in 32-bit IDA or you won't be able to decompile. The problem statement gives some bytes,

```
71, 66, 61, 42, 53, 45, 7A, 40, 51, 4C, 5E, 30, 79, 5E, 31, 5E, 64, 59, 5E, 38, 61, 36, 65, 37, 63, 7C,
```

This function is pretty simple: main passes the input to `encrypt_flag(char*)`, then prints out the result as series fo hex values. So what does `encrypt_flag` do?

```
char *__fastcall encryptFlag(char *result)
{
  char v1; // r3
  int v2; // t1

  v1 = *result;
  if ( *result )
  {
    do
    {
      *result = v1 - 1;
      v2 = (unsigned __int8)(result++)[1];
      v1 = v2;
    }
    while ( v2 );
  }
  return result;
}
```

It loops through the bytes and adds one to each. Great. So take the given array, look each character up in [http://asciitable.com], look one previous, and write that down. Honestly it was faster that way than automating it. And you get the flag!

### Author
[timeroot](https://github.com/timeroot)