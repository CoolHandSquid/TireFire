#!/usr/bin/python3
from pathlib import Path
import os

path = Path(__file__ + '../..').resolve()
#arrow = top / 'assets/arrow.png'
#print('source image:', arrow)
#print('destination image:', top / 'output' / os.path.basename(arrow))
print(path)
os.system("python3 {}/dirsearch/dirsearch.py -w /Yeet/Tools/TireFire/Wordlists/dir_medium.txt -e php -f -t 20 -u http://10.10.10.181".format(path))