# Keen Eye
## Challenge Description
Pay close attention... http://challenge.rgbsec.xyz:8376/

## Solution

Nothing in the linked website appears out of the ordinary. There is a web form,
but there is also a comment that the form does nothing. There is also a small
amount of javascript.

```
<script type="text/javascript">
    window.onerror = function (message, url, lineNumber) {
        return true;
    };
</script>
```

It appears that this javascript is included to hide some error. We create a
duplicate HTML page which excludes this javascript and reload the page.
This reveals an error in the Developer Console:

```
Uncaught SyntaxError: export declarations may only appear at top level of a module popper.min.js:4:19739
```

We navigate to the linked popper.min.js and find a minified javascript file.
We search for the string "rgb" and find the flag.


## Flag
```rgbctf{n073_7h3_d1ff}```

### Author
[keegan](https://twitter.com/inf_0_)