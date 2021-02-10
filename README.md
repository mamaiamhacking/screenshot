# Introduction

A simple python screenshot tool in linux. 

# Installation

Require `firefox`, `selenium`, `geckodriver`.

Corsy only works with `Python 3` and has the following depencies:

* [Firefox](https://support.mozilla.org/en-US/kb/install-firefox-linux).
* selenium & Pillow
    ```
    python3 -m pip install selenium --upgrade
    python3 -m pip install Pillow --upgrade
    ````
* [geckodriver](https://github.com/mozilla/geckodriver/releases)


For ubuntu:
```
sudo bash install.sh
```

# Usage

Example:
```
mkdir images
python3 screenshot.py -u https://www.google.com -t webp -o ./images/google -q 50
ls images
# google.webp
```

# Options

```
usage: python3 screenshot.py [-h] [-u URL] [-o OUTPUT] [-t FILETYPE] [-q QUALITY]

optional arguments:
  -h, --help   show this help message and exit
  -u URL       Target url.
  -o OUTPUT    Output file name.
  -t FILETYPE  File type. png webp jpeg...
  -q QUALITY   Quality. 0-100. Default 50
```