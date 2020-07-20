# Laser 2 - Sorting
## Challenge Description
https://github.com/Quintec/LaserLang

Here's a harder Laser challenge. Given an input stack of numbers, sort them in descending order. nc challenge.rgbsec.xyz 7678

Input: 1 2 7 3 ~~down the rockefeller street~~

Output: 7 3 2 1

## Solution
(See Laser1.md for some general tips on writing good Laser code.)

We sort through a version of selection sort, see https://en.wikipedia.org/wiki/Selection_sort. We have a list of "remaining" numbers (stacks 0/1), and a sorted list of "selected" numbers (stack 2). These are initially the given input, and empty, respectively.

In each step, we want to pick out the smallest number from the remaining ones, and put it on top of our "selected" stack. So we take the first number from "remaining" (in stack 0) and move to "selected". Then we go one by one through each "remaining" number, moving them to stack 1 as we do so. Each time we move one from stack 0 to stack 1, we compare it with stack 2; if the number on stack 1 is smaller than on stack 2, we swap them. In this way, by the time stack 0 is empty, the smallest number has been put on stack 2.

Then we copy stack 1 back to stack 0 for the next loop.

We do this until the "remaining" list is empty, at which point stack 2 has been sorted. We return stack 2.

Code:
```
I> c'1'g ⌝p sUs >DsU r UrwD l⌝psUswUwDD> DcsU'0'g  !⌝p     >c⌝pw \>D  \ 
                             \p        /                   \     /
                \                                  p/        \p   /    
 \                                                                    /
         p
         \ sUsU #

take input to stack 0
find smallest element:
 move top element to stack 2
 loop:
  move top of 0 to 1
  duplicate top of 1
  copy top of 2 to 1
  compare. if smaller,
   pop
   swap top of 1 and 2
  else,
   pop
  check stack 0 cardinality
  if NOT 0, loop
 
 #copy stack 1 back to stack 0
 check stack 1 cardinality
 if 0, skip:
  move top of 1 to 0
  go back to check
 
 check stack 0 cardinality
 if NOT 1, main loop

move last thing up 
return on stack 2
```

### Author
[timeroot](https://github.com/timeroot)
