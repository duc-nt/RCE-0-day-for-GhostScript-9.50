# RCE-0-day-for-GhostScript-9.50

### PoC for RCE 0-day for GhostScript 9.50 - Payload generator
### The PoC in python generates payload when exploited for a 0-day of GhostScript 9.50. This 0-day exploit affect to ImageMagick with the default settings from Ubuntu repository (Tested with default settings of ImageMagick on Ubuntu 20.04)

### This project is created only for educational purposes and cannot be used for law violation or personal gain.
### The author of this project is not responsible for any possible harm caused by the materials of this project. 

### Original finding and awesome research from Emil Lerner: https://twitter.com/emil_lerner/status/1430502815181463559

### Usage: `python IM-RCE-via-GhostScript-9.5.py <CMD> <Exploit-File>`

## Demo
<img src="https://pbs.twimg.com/media/E-h9HtGVkAk0IVW?format=png&name=large">

## Noted for php-imagemagick, sometime you must find the correct `fd/<number>`. The easiest way for doing this stuff is fuzzylogic and something like this (Tested with Ubuntu 20.04 and default php-imagemagick installed).
<img src="https://pbs.twimg.com/media/E-iOJt_VIAAKmBi?format=png&name=large">

