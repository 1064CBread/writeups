# Too Slow
## Challenge Description
I've made this flag decryptor! It's super secure, but it runs a little slow.

File: a.out

## Solution
We're given a binary which, we are told, will output the flag, albeit very slowly. The binary has two ffunctions: `generate_key()`, which returns an int32, and `win()`, which takes that int32 and generates the key. Figuring that `generate_key()` will probably be the slow part, let's reverse that first. Hex-Rays gives

```
__int64 generate_key()
{
  int v0; // eax
  __int64 v2; // [rsp-8h] [rbp-8h]

  __asm { endbr64 }
  for ( *((_DWORD *)&v2 - 2) = 0; *((_DWORD *)&v2 - 2) <= 0x265D1D22u; ++*((_DWORD *)&v2 - 2) )
  {
    for ( *((_DWORD *)&v2 - 1) = *((_DWORD *)&v2 - 2); *((_DWORD *)&v2 - 1) != 1; *((_DWORD *)&v2 - 1) = v0 )
    {
      if ( *((_DWORD *)&v2 - 1) & 1 )
        v0 = 3 * *((_DWORD *)&v2 - 1) + 1;
      else
        v0 = *((_DWORD *)&v2 - 1) / 2;
    }
  }
  return *((unsigned int *)&v2 - 2);
}
```

Prettifying that a bit:


```
__int32 generate_key()
{
  __int32 X;
  __int32 Y;

  for ( X = 0; X <= 0x265D1D22u; ++X )
  {
    for ( Y = X; Y != 1; )
    {
      if ( Y%2 == 1 )
        Y = 3 * Y + 1;
      else
        Y = Y / 2;
    }
  }
  return *X;
}
```

It's pretty clear that `Y` doesn't enter the picture at all, it's just computing a Collatz sequence in `Y`, starting with `X`, and will do this for every `X` up through `0x265D1D22u`. Thus, this program will return `0x265D1D23u`.

`win(__int32 X)` is simpler:

```
 v5 = 0x12297E12426E6F53LL;
  v6 = 0x79242E48796E7141LL;
  v7 = 0x49334216426E2E4DLL;
  v8 = 0x473E425717696A7CLL;
  v9 = 0x42642A41;
  v10 = 0;
  for ( i = 0; i <= 8; ++i )
    *((_DWORD *)&v5 + i) ^= X;
  printf("Your flag: rgbCTF{%36s}\n", &v5);
```

These hexadecimal constants are a way to load bytes on the stack: they're the flag XORed with the key `X`. To get the flag, let's quickly rewrite it in [java](too_slow.java).

Giving the flag `rgbCTF{pr3d1ct4bl3_k3y_n33d5_no_w41t_cab79d}`.

### Author
[timeroot](https://github.com/timeroot)