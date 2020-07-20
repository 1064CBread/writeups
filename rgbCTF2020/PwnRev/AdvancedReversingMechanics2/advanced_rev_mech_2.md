# Advanced Reversing Mechanics 2
## Challenge Description
More advanced than very very advanced
`0A, FB, F4, 88, DD, 9D, 7D, 5F, 9E, A3, C6, BA, F5, 95, 5D, 88, 3B, E1, 31, 50, C7, FA, F5, 81, 99, C9, 7C, 23, A1, 91, 87, B5, B1, 95, E4,`

File: arm_hard.o

## Solution
This problem is similar in structure to ARM1, but `encrypt_flag()` looks considerably more complicated:

```
_BYTE *__fastcall encryptFlag(_BYTE *result)
{
  unsigned int v1; // r3
  _BYTE *i; // r1
  int v3; // r3
  bool v4; // zf
  unsigned int v5; // r3
  unsigned int v6; // r2
  __int64 v7; // r2

  v1 = (unsigned __int8)*result;
  if ( *result )
  {
    for ( i = result; ; v1 = (unsigned __int8)*i )
    {
      v6 = (unsigned __int8)(v1 - 10);
      if ( v1 <= 'O' )
      {
        LOBYTE(v1) = v1 + 'F';
        if ( v6 <= 'P' )
          LOBYTE(v1) = v6;
      }
      *i++ = (((unsigned __int8)(v1 - 7) ^ 0x43) << 6) | ((unsigned __int8)((v1 - 7) ^ 0x43) >> 2);
      v7 = i - result;
      if ( !*i )
        break;
      v3 = v7 - 5 * (((signed int)((unsigned __int64)(0x66666667LL * (signed int)v7) >> 32) >> 1) - HIDWORD(v7));
      v4 = v3 == 2;
      v5 = (((unsigned __int8)*i << (-(char)v3 & 7)) | ((unsigned int)(unsigned __int8)*i >> v3)) & 0xFF;
      if ( v4 )
        LOBYTE(v5) = v5 - 1;
      *i = v5;
    }
  }
  return result;
}
```

... but why reverse when we can black-box? Some playing around reveals that the Nth character of output only depends on the first N characters of input. So let's use this function, encrypt_flag, as an oracle, and try progressively longer things until we get our goal. We write a solver: [here](solver.c)

and it outputs

```
Len 35
So far r
So far rg
So far rgb
So far rgbC
So far rgbCT
So far rgbCTF
So far rgbCTF{
So far rgbCTF{A
So far rgbCTF{AR
So far rgbCTF{ARM
So far rgbCTF{ARM_
So far rgbCTF{ARM_a
So far rgbCTF{ARM_ar
So far rgbCTF{ARM_ar1
So far rgbCTF{ARM_ar1t
So far rgbCTF{ARM_ar1th
So far rgbCTF{ARM_ar1thm
So far rgbCTF{ARM_ar1thm3
So far rgbCTF{ARM_ar1thm3t
So far rgbCTF{ARM_ar1thm3t1
So far rgbCTF{ARM_ar1thm3t1c
So far rgbCTF{ARM_ar1thm3t1c_
So far rgbCTF{ARM_ar1thm3t1c_r
So far rgbCTF{ARM_ar1thm3t1c_r0
So far rgbCTF{ARM_ar1thm3t1c_r0c
So far rgbCTF{ARM_ar1thm3t1c_r0ck
So far rgbCTF{ARM_ar1thm3t1c_r0cks
So far rgbCTF{ARM_ar1thm3t1c_r0cks_
So far rgbCTF{ARM_ar1thm3t1c_r0cks_f
So far rgbCTF{ARM_ar1thm3t1c_r0cks_fa
So far rgbCTF{ARM_ar1thm3t1c_r0cks_fad
So far rgbCTF{ARM_ar1thm3t1c_r0cks_fad9
So far rgbCTF{ARM_ar1thm3t1c_r0cks_fad96
So far rgbCTF{ARM_ar1thm3t1c_r0cks_fad961
So far rgbCTF{ARM_ar1thm3t1c_r0cks_fad961}
rgbCTF{ARM_ar1thm3t1c_r0cks_fad961}
```

### Author
[timeroot](https://github.com/timeroot)