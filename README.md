insta-like-counter
======
A Python script that adds up the total number of likes across all your Instagram photos.

Requires
-----
  * [python-instagram](https://github.com/Instagram/python-instagram)
  * [python-progressbar](http://code.google.com/p/python-progressbar/)
  
Usage
-----

  1. Obtain an access token (e.g. using Instagram's [get_access_token.py](https://github.com/Instagram/python-instagram/blob/master/get_access_token.py))
  2. Save the access token to a text file named `token.txt`
  3. Run `insta-like-counter.py` to get the total likes for your own photos or `insta-like-counter.py username` to get total likes for someone else's photos 