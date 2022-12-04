I often find myself working at my computer, and have to pull out my phone to get my 2FA code for google or whatever.  what a hassle.

After four seconds of googling, I did not immediately find a desktop based 2fa app, so instead I spent a couple hours writing my own.

This is really just an unnecessarily verbose frontend for <a href="https://pyauth.github.io/pyotp/">pyotp</a> (<a href="https://github.com/pyauth/pyotp">github</a>).

#
Note: I do not recommend that anybody actually use this, as it stores a secret account key in an unencrypted database.
It is only useful for those of us who are lazier than we are concerned about online security.  
<br>I may try to fix this in the future.

#
## instructions
execute `pip install -r requirements.txt` then `python main.py`.
<br>Click on Add new account.
<br>Go to set up a 2fa app on google or reddit or wherever, and it will give you a secret setup key.  Enter that in this app, and click OK.
<br>It'll also be able to generate a QR code, which you can scan with a 2FA app on your phone like Authenticator.

#

to do:
<br>add shortcuts, e.g. Ctrl+C, and right click > copy code.