#!/usr/bin/env python3
"""Download licensed Wikimedia Commons photographs for offline Henosis; no dependencies."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote


FILES = [('anu', 'Cuneiform tablet- commentary on Enuma Anu Enlil, tablet 5 MET DP-442-001.jpg'), ('enlil', 'God Enlil, seated, from Nippur, Iraq. 1800-1600 BCE. Iraq Museum.jpg'), ('enki', 'God Ea, seated, holding a cup. From Nasiriyah, Iraq, 2004-1595 BCE. Iraq Museum.jpg'), ('nabu', 'En profile. Statue of god Nabu, from Nimrud, Iraq, 8th century BCE. Iraq Museum.jpg')]
DEST=Path(__file__).resolve().parent/'assets'
DEST.mkdir(exist_ok=True)
for short, filename in FILES:
    url='https://commons.wikimedia.org/wiki/Special:FilePath/'+quote(filename,safe='')+'?width=960'
    print('Downloading',short,'...',flush=True)
    req=Request(url,headers={'User-Agent':'HenosisSiteBuilder/1.4 (personal website; image attribution in PHOTO_CREDITS.txt)'})
    try:
        with urlopen(req,timeout=35) as r: data=r.read()
        if not data.startswith(b'\xff\xd8\xff'):
            raise ValueError('Server did not return a JPEG image')
        (DEST/(short+'.jpg')).write_bytes(data)
        print('Saved',DEST/(short+'.jpg'))
    except Exception as e:
        print('FAILED',short,':',e)
print('Done. Refresh Firefox with Ctrl+Shift+R.')
