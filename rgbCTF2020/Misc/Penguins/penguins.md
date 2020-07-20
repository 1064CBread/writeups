# Penguins
## Challenge Description
*waddle waddle*

File: 2020-06-29-173949.zip

## Solution
You are given a git repo with some irrelevant files and red herrings. The `COMMIT_EDITMSG` says "some things are not needed", which implies this repo previously contained the flag but no longer does. Looking at history with `git reflog`, there are several possibly relevant commits.

```
27440c5 (master) HEAD@{11}: reset: moving to HEAD
27440c5 (master) HEAD@{12}: checkout: moving from fascinating to master
800bcb9 HEAD@{13}: commit: some things are not needed
57adae7 (HEAD) HEAD@{14}: commit: relevant file
fb70ca3 HEAD@{15}: commit: probably not relevant
5dcac0e HEAD@{16}: commit: another perhaps relevant file
b474ae1 HEAD@{19}: checkout: moving from b474ae165218fec38ac9fb8d64f452c1270e68ea to fascinating
b474ae1 HEAD@{20}: checkout: moving from master to b474ae1
27440c5 (master) HEAD@{21}: commit (merge): Merge branch 'feature1'
102b03d HEAD@{22}: commit: some more changes
b474ae1 HEAD@{23}: commit: some new info
8ee6237 HEAD@{24}: commit: added an interesting file
```

Checking out commits and inspecting files reveals most of them to be bait.
However, the commit `57adae7` contains the base64-encoded file `perhaps_relevant_v2`, which when decoded gives

```
as yoda once told me "reward you i must"
and then he gave me this ----
rgbctf{d4ngl1ng_c0mm17s_4r3_uNf0r7un473}
```

### Author
jellybeans