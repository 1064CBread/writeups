# Differences
## Challenge Description
If a difference could difference differences from differences to calculate
differences, would the difference differently difference differences to
difference the difference from different differences differencing?

File: DifferenceTest.java

## Solution

Opening DifferenceTest.java in a text editor immediately reveals it to be a
corrupted Java source file. However, it's pretty easy to guess what the
uncorrupted file would be:

    import java.util.*;
    public class DifferenceTest {
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();
        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();
        int answer = num1 - num2;
        System.out.println("The difference is: " + answer);
      }
    }

I saved this file as DifferenceReal.java.

Given the wording of the prompt, I guessed that the next step would be to
calculate the differences between the corrupted and uncorrupted ASCII values,
so I passed both files through `xxd`:

    $ xxd -p DifferenceTest.java
    696d706f72e620d1c376612e7574696c2e2a3b0a70b8626c69b720636c61
    737320446966666572656e636554657374207b0a09707562b26963207374
    6174696320766f6964206d61696e28537472696e675bd820617267732920
    7b0a09095363616e6e657220e7d5203d209f6577205363616eded1722853
    79a6d3656d2e696e293b0a090953797374656d2e6f75742e7072696ee128
    22456e746572206669727374206e756d6265723a2022293b0a0909696e74
    206e756d31203d2073632e6e657874496e7428293b0a090953797374656d
    2e6f75742e707269a1742822456e746572207365636f6e6420a2756d6265
    723a2022293b0a0909696e74206e756d32203d2073632e6e6578e2499f74
    28293b0a0909696e7420616e73776572203d206e756d31202d206e756d32
    3b0a0909c1797374656d2e6f75742ed772696e746c6e2822546865206469
    66666572656e63652069733a2022202b20616e73776572293b0a097d0afa
    $ xxd -p DifferenceReal.java
    696d706f7274206a6176612e7574696c2e2a3b0a7075626c696320636c61
    737320446966666572656e636554657374207b0a097075626c6963207374
    6174696320766f6964206d61696e28537472696e675b5d20617267732920
    7b0a09095363616e6e6572207363203d206e6577205363616e6e65722853
    797374656d2e696e293b0a090953797374656d2e6f75742e7072696e7428
    22456e746572206669727374206e756d6265723a2022293b0a0909696e74
    206e756d31203d2073632e6e657874496e7428293b0a090953797374656d
    2e6f75742e7072696e742822456e746572207365636f6e64206e756d6265
    723a2022293b0a0909696e74206e756d32203d2073632e6e657874496e74
    28293b0a0909696e7420616e73776572203d206e756d31202d206e756d32
    3b0a090953797374656d2e6f75742e7072696e746c6e2822546865206469
    66666572656e63652069733a2022202b20616e73776572293b0a097d0a7d

I already had Firefox open, so I figured I'd do the rest in the JavaScript
console. First, I chunked the hexdump into groups of two:

    const a = '696d706f72e620d1c376612e7574696c2e2a3b0a70b862...'.match(/../g);
    const b = '696d706f7274206a6176612e7574696c2e2a3b0a707562...'.match(/../g);
    
Next, I constructed an array with the differences:

    const t = [];
    
    for (i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        t.push((parseInt(a[i], 16) - parseInt(b[i], 16)));
      }
    }

Parsing the resulting numbers as ASCII values produced the flag:

    t.map(d => String.fromCharCode(d)).join('');


## Flag
`rgbCTF{tr1pl3_m34n1ng}`

### Author
[DeepToaster](https://github.com/deeptoaster)