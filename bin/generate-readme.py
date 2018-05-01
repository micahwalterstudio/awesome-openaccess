#!/usr/bin/env python

import sys
import os
import os.path
import yaml
import json
import glob
import pprint

if __name__ == '__main__':

    whoami = os.path.abspath(sys.argv[0])
    bindir = os.path.dirname(whoami)
    datadir = os.path.dirname(bindir)
    datadir = os.path.join(datadir, 'data')

    readme = open('README.md', 'w')
    
    readme.write('# Awesome OpenAccess\n')
    readme.write('[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)')
    readme.write('\n')
    readme.write('*An awesome list of awesome OpenAccess projects*\n')
    
    ## read in all the yml files

    datafiles = {}
    
    for filename in glob.glob(datadir + '/*.yml'):
        stream = file(filename, 'r')
        yml = yaml.load(stream)
        head, tail = os.path.split(filename)
        tail = os.path.splitext(tail)[0]
        datafiles[tail] = yml
    
    for org in sorted(datafiles.iterkeys()):    
        pprint.pprint(datafiles[org]['name'])
        readme.write('* [' + datafiles[org]['name'] + '](' + datafiles[org]['url'] + ')\n' )

    readme.close()     
