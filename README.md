# Twitter Broadcast Downloader
Download Twitter broadcasts/lives. 

## How does it work?
Input an URL (e.g. https://twitter.com/i/broadcasts/s0M3th1nG) 
The script will then run Selenium to get the ".m3u8 address" which is most likely hosted on xxx.
This address is loaded after the page has loaded in, so the script adds an event listener to listen for all XMR events and adds the response to a long string. This string is saved under `document.sniffed`, because we need it to be accessiable from the other script we are going to run. Variables ran through `execute_script` (e.g. `var sniffed = ""`) are local, therefore we cannot access it from `execute_script`.
It is critical that the event listener script is injected before the data for the broadcast (".m3u8 address") is received.
The string (`document.sniffed`) is looped through and we try to find the .m3u8 address, which is done by checking if one of the values in the string includes `master_dynamic_`.
This address is returned into main, and downloaded through FFMPEG.
You could also copy the address, and play it through VLC, if you just want to view the broadcast "locally".

## Installation
```
pip install -r "requirements.txt"
```
FFMPEG is also required and has to be added to path.

