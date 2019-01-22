#!/usr/bin/env python

import sys
import os
import os.path
import yaml
import json
import glob
import pprint

def text2emoji(text):
    
    emoji = ''

    for thing in sorted(text):
        if thing == 'images':
            emoji = emoji + ':camera: '
        if thing == 'iiif':
            emoji = emoji + ':minidisc: '
        if thing == 'csv':
            emoji = emoji + ':blue_book: '
        if thing == 'tsv':
            emoji = emoji + ':green_book: '
        if thing == 'xml':
            emoji = emoji + ':closed_book: '
        if thing == 'xls':
            emoji = emoji + ':notebook: '
        if thing == 'json':
            emoji = emoji + ':orange_book: '
        if thing == 'api':
            emoji = emoji + ':computer: '
 
    
    print(emoji)
    
    return emoji

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
    readme.write('\n')
    readme.write('This is an awesome list of awesome OpenAccess projects. If you\'d like to contribute, please read the guidlines in [CONTRIBUTING.md](https://github.com/micahwalterstudio/awesome-openaccess/blob/master/CONTRIBUTING.md)\n')
    
    ## legend
    
    readme.write('### Key\n')
    readme.write('| Emoji | Meaning |\n')
    readme.write('| --- | --- |\n')
    readme.write('| :octocat: | GitHub Repo |\n')
    readme.write('| :globe_with_meridians: | Documentation Website |\n')
    readme.write('| :camera: | Images |\n')
    readme.write('| :minidisc: | IIIF Images |\n')
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
        stream = open(filename, 'r')
        yml = yaml.load(stream)
        head, tail = os.path.split(filename)
        tail = os.path.splitext(tail)[0]
        datafiles[tail] = yml
    
    readme.write('| Organization | Location | Data |\n')
    readme.write('| --- | --- | --- |\n')
    
    for org in sorted(datafiles.keys()):    
        pprint.pprint(datafiles[org]['name'])
        links = ''
        if 'url' in datafiles[org]:
            links = links + '[:globe_with_meridians:](' + datafiles[org]['url'] +') '
        if 'github' in datafiles[org]:
            links = links + '[:octocat:](' + datafiles[org]['github'] +') '
            
        emoji = text2emoji(datafiles[org]['data'])
        readme.write('| [' + datafiles[org]['name'] + '](' + datafiles[org]['url'] + ') | ' + datafiles[org]['location'] + ' | ' + links + emoji +' |  \n' )

    readme.close()     
