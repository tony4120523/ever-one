# ever-one

read a note randomly from the Evernote account.

require the Evernote [API key](https://dev.evernote.com/)

# usage
```
$ pip install virtualenv
```
```
$ git clone https://github.com/tony4120523/ever-one.git
```
```
$ cd ever-one
```
```
$ virtualenv venv
$ source venv/bin/activate
$ virtualenv --python=/usr/bin/python2.7 venv
```
```
$ pip install evernote flask thrift
```
modify the `client.py` file in dir  `~/venv/lib/python2.7/site-packages/evernote/api/client.py` 

in line 159, change `addHeader` into `setCustomHeader` and delete the `"**"`

fill the user name, user secret in `webserver.py`
```
$ python webserver
```
click the link, open the website by browser.
authenticate the application permission.
get the `auth_token` from terminal.
open `get_one.py` file and fill the `auth_token` and the `notebook_name` in `get_one.py` file.
```
$ python get_one.py > note.html
$ google-chrome note.html
```
```
$ deactivate
```
try to run above command via the `./one.sh` script (optional)
