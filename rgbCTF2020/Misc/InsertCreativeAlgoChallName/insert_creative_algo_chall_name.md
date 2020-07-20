# [insert clever algo chall name]
## Challenge Description
[https://pastebin.com/pKNVLkTs](https://pastebin.com/pKNVLkTs)

## Solution

Note that the sum of any set of nonnegative-integer powers of two is a unique
nonnegative integer. (In fact, it's *every* nonnegative integer---this is
literally how binary numbers are constructed.) So basically, the problem
statement is equivalent to asking for the number of distinct partitions of *n*
elements into *k* subsets.

This can be calculated by induction. Consider the set *S*(*n*,*k*) of distinct
partitions of a set *N*(*n*) of *n* elements into *k* subsets, and let
#*S*(*n*,*k*) be its cardinality. Observing the rightmost element *x* of
*N*(*n*) without loss of generality, we see that for every partition in
*S*(*n*,*k*), *x* is either in a subset on its own (a singleton) or in a subset
with one or more other elements of *N*(*n*).

*   If *x* is in a subset on its own, then removing it leaves *n*–1 elements
    partitioned into *k*–1 subsets. So the number of distinct partitions in
    which *x* is in a subset on its own is #*S*(*n*–1,*k*–1).
*   If *x* is in a subset with one or more other elements of *N*(*n*), then
    removing it leaves *n*–1 elements partitioned into *k* subsets. But for
    each of the remaining *k* subsets, *x* could have been taken from any of
    them. So the number of distinct partitions in which *x* is in a subset with
    one or more other elements is *k*#*S*(*n*–1,*k*).
    
So #*S*(*n*–1,*k*)=#*S*(*n*–1,*k*–1)+*k*#*S*(*n*–1,*k*).

I already had Firefox open, so I figured I'd do the rest in the JavaScript
console. #*S*(12,4) turned out to be too deep to calculate recursively, so I
tried again with an iterative approach:

    const s = {};
    
    for (let n = 3; n <= 12; n++) {
      for (let k = 2; k < n; k++) {
        s[`${n},${k}`] =
            (k !== 2 ? s[`${n - 1},${k - 1}`] : 1) + 
            k * (k !== n - 1 ? s[`${n - 1},${k}`] : 1);
      }
    }
    
Note that the `k === 2` case comes from the fact that #*S*(*n*–1,1) (the number
of ways to partition a set into one subset) is always one, and that the `k ===
n - 1` case comes from the fact that #*S*(*n*–1,*n*–1) (the number of ways to
partition a set into as many subsets as it has elements) is always one.

This constructs a table of the following form:

|         |  2 |  3 |  4 | . | . | . | *k* |
| ------- | -- | -- | -- | - | - | - | --- |
|   **3** |  3 |    |    |   |   |   |     |
|   **4** |  7 |  6 |    |   |   |   |     |
|   **5** | 15 | 25 | 10 |   |   |   |     |
|  **.**  |    |    |    | . |   |   |     |
|  **.**  |    |    |    |   | . |   |     |
|  **.**  |    |    |    |   |   | . |     |
| ***n*** |    |    |    |   |   |   |     |

`s['12,4']` contains the answer.

(I learned later on that these are known as the [Stirling numbers of the second
kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind), and
that the answer is [readily available on OEIS](https://oeis.org/A000453).)


## Flag
`rgbCTF{611501}`

### Author
[DeepToaster](https://github.com/deeptoaster)