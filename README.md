# MPC-media-audit
Semi automated media curation, windows media player classic. Python, selenium, Windows media player classic.
MPC Python:
Running this with media player class open and a playlist loaded will skip through the media files, the start, 25% 50% 75% and ending. User can set delete hotkeys or mark for deletion with Hotkey listener. Used to audit large collections of media, media file positions to sample can be adjusted, changing the volume to zero increases the skipping speed to maximum, increasing volume to maximum halts automated skipping. Adjusting media seeking manually also halts skipping until seek is at the start of the file. Requires selenium, python, chromedriver, media player classic with a playlist already playing media. Tip: use hardlinks to create super directory then load all files from super directory with mpcs open folder. *See also addtional MPC playlist builder to sort by accessed and size by this author. 

Hotkey Listen:
Run this to listen to a specified keypress, pressing this key whilst MPC Python is running will read the currently playing media's file path and append to a stored list that can be manually deleted or reviewed. Default key is *. MPC Python must be running. 

KillDrivers:
Incase python WMI fails to kill the chromedriver after MPC python stops. 

toDelete:
Can open delete list, or run to delete files tagged. 
