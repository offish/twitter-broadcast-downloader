# Twitter Broadcast Downloader
Download Twitter broadcasts/lives. 

## How does it work?
Input an URL (e.g. https://twitter.com/i/broadcasts/s0M3th1nG).
The script will then run Selenium to get the ".m3u8 address" which is hosted on `<something>.video.pscp.tv` or something similar.
The address we are looking for is loaded after the page has loaded in, so the script adds an event listener to listen for all XHR events and try to find the m3u8.
If the listener finds the data that includes the m3u8 address, it will throw an error to the console, where the Python script is listening for errors.
If the error includes the m3u8 address it will extract it and download it through FFMPEG.
You could also copy the address, and play it through VLC, if you just want to view the broadcast "locally".

## Installation
```
pip install -r "requirements.txt"
```
FFMPEG is also required and has to be added to path.

