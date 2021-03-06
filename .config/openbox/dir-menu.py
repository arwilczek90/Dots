#!/usr/bin/python

import os
import random
from sys import argv

mypath = argv[0]

def ext_resolver(filename):
    ext = filename.split('.')[-1]
    ext = ext.lower()
    ext_list = {'nes':'tuxnes -E --js1=/dev/input/js0 --joystick-map=1:B2,B1,B9,B8,,,,,B3',
                'smc':'zsnes -m -v 18 -y',
                'gba':'VisualBoyAdvance',
                'bin':'dgen -f -j',
                'ape':'vlc',
                'flac':'vlc',
                'ogg':'vlc',
                'ogm':'vlc',
                'mp3':'vlc',
                'avi':'vlc',
                'divx':'vlc',
                'm4a':'vlc',
                'm4v':'vlc',
                'mkv':'vlc',
                'mp4':'vlc',
                'vob':'vlc',
                'py' :'gksudo geany',
                'png':'mirage',
                'jpg':'mirage',
                'bmp':'mirage',
                'gif':'mirage',
                'svg':'mirage',
                'tex':'geany',
                'txt':'geany',
                'xml':'geany',
                'pdf':'xournal',
				'ps':'xournal',
                'html':'x-www-browser',
                'html5':'x-www-browser',
				'deb':'gdebi',
                'desktop':'gksudo geany',
                'sh':'gksudo geany',
                'exe':'wine start /unix',
				'jar':'java -jar'}
    if ext in ext_list:
        return ext_list[ext]
    else:
        return 'echo'

def dir_list(dircontent):
    dirs = []
    files = []
    for item in dircontent:
        if os.path.isdir(currentpath + '/' + item):
            dirs.append(item)
        else:
            files.append(item)
    dirs.sort()
    files.sort()
    return dirs, files

def replacer(string):
    return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')

def gen_menu(dirs, files):
    curpath = replacer(currentpath)
    print('<openbox_pipe_menu>')
    
    print('<item label="Open in Nemo"><action name="execute"><execute>nemo "' + curpath + '"</execute></action></item>')
    print('<separator />')
    
    for thisdir in dirs:
        thisdir = replacer(thisdir)
        menuid = str(random.randrange(1,99,1)).zfill(2)
        print('  <menu execute="' + mypath + ' ' + curpath + '/' + thisdir + '" id="' + thisdir + "-" + menuid + '" label="' + thisdir + '"/>')
        
    for thisfile in files:
        thisfile = replacer(thisfile)
        print('  <item label="' + thisfile + '">')
        print('    <action name="execute">')
        print('      <execute>')
        print('        ' + ext_resolver(thisfile) + ' "' + curpath + '/' + thisfile + '"')
        print('      </execute>')
        print('    </action>')
        print('  </item>')
    print('</openbox_pipe_menu>')

if len(argv) > 1:
    currentpath = ' '.join(argv[1:])
else:
    currentpath = "/"

try:
    content = [x for x in os.listdir(currentpath) if x[0] != '.']
    parts = dir_list(content)
    gen_menu(parts[0], parts[1])
except OSError:
    print('<openbox_pipe_menu>')
    print('<separator label="No access" />')
    print('</openbox_pipe_menu>')