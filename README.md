# ever-one

read a note randomly from the Evernote account.

require the Evernote __FULL ACCESS__ [API key](https://dev.evernote.com/) 

# usage
```
$ pip install virtualenv
```
```
$ mkdir vir
$ cd vir
$ git clone https://github.com/tony4120523/ever-one.git
```
```
$ virtualenv venv
$ source venv/bin/activate
$ virtualenv --python=/usr/bin/python2.7 venv
```
install some library
```
$ pip install evernote flask thrift
```
modify the `client.py` file in dir  `~vir/venv/lib/python2.7/site-packages/evernote/api/client.py` 

in line 22, change __True__ into __False__

in line 159, change `addHeader` into `setCustomHeader` and delete the `"**"`

fill the __user name, user secret__ (API key) in `webserver.py`
```
$ python webserver.py
```
click the authentication link, open the website by browser.

authenticate the application permission.

get the `auth_token (S=XXXX...)` from terminal.

fill the `auth_token`, `notebook_name` in `get_one.py` file.
```
$ python get_one.py > note.html
$ google-chrome note.html
```
```
$ deactivate
```
try to run above command via the `./one.sh` script (optional)
# reference
* https://github.com/nilshamerlinck/random-evernote
* https://github.com/paultopia/minimal-evernote-oauth
