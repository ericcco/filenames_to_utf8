import os
from glob import glob
import shutil
import urllib

files = glob(u'*.txt')
for my_file in files:
    try:
        print "File %s" % my_file
    except UnicodeEncodeError:
        print "File (escaped): %s" % my_file.encode("unicode_escape")
    old_name = my_file
    new_name = my_file
    try:
        my_file.encode(" CP1252" , "strict")
        print "    Name unchanged"
    except UnicodeEncodeError:
        print "    Name changed"
        utf_8_name = my_file.encode("UTF-8")
        new_name = urllib.quote(utf_8_name )
        print "    New name: (%% encoded): %s" % new_name

    os.rename(old_name,new_name)
