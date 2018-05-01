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
    readme.write('[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)\n')
    readme.write('\n')
    readme.write('*An awesome list of awesome OpenAccess projects* \n')
    
    ## legend
    
    readme.write('### Key\n')
    readme.write('| Emoji | Meaning |\n')
    readme.write('| --- | --- |\n')
    readme.write('| :octocat: | GitHub Repo |\n')
    readme.write('| :globe_with_meridians: | Documentation Website |\n')
    readme.write('| :camera: | Images |\n')
    readme.write('| :blue_book: | CSV Dataset |\n')
    readme.write('| :green_book: | TSV Dataset |\n')
    readme.write('| :closed_book: | XML Dataset |\n')
    readme.write('| :notebook: | XLS Dataset |\n')
    readme.write('| :orange_book: | JSON Dataset |\n')
    readme.write('| :computer: | API |\n')

    readme.write('### Datasets\n')

    
    ## read in all the yml files

    datafiles = {}
    
    for filename in glob.glob(datadir + '/*.yml'):
        stream = file(filename, 'r')
        yml = yaml.load(stream)
        head, tail = os.path.split(filename)
        tail = os.path.splitext(tail)[0]
        datafiles[tail] = yml
    
    readme.write('| Organization | Data | Description |\n')
    readme.write('| --- | --- | --- |\n')
    
    for org in sorted(datafiles.iterkeys()):    
        pprint.pprint(datafiles[org]['name'])
        readme.write('| [' + datafiles[org]['name'] + '](' + datafiles[org]['url'] + ') | stuff | description words go here |  \n' )

    readme.close()     
