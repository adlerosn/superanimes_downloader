#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:31:43 2015

@author: adler
"""

from os.path import isfile as isfile
from os.path import isdir as isdir
import sys
from os import popen as system

animeinfofilelocation='animeInfo.txt'

def parseInfo(string):
    l=[k.split(': ')[1] for k in string.strip().strip('\n').strip().split('\n')]
    l[2]=int(l[2])
    l[3]=int(l[3])
    return l

def readAllFile(loc):
    f=open(loc,'rt')
    a=f.read()
    f.close()
    return a

def readList(loc):
    return [a for a in readAllFile(loc).strip('\n').strip(' ').strip('\n').split('\n')]

def saveList(loc,lst):
    f=open(loc,'wt')
    for t in lst:
        f.write(t+'\n')
    f.close()

def run(cmd):
    return system('bash -c "'+cmd+'"').read()

def runbkg(cmd):
    return system('bash -c "'+cmd+'"')

def download(url):
    run('wget '+url+' -O tmpfile.tmp')
    a=readAllFile('tmpfile.tmp')
    run('rm tmpfile.tmp')
    return a

def downloadToFile(url,fn):
    run('wget '+url+' -O '+fn)
    
def downloadToFileContinuing(url,fn):
    if isfile(fn):
        run('wget '+url+' -c -O '+fn)
    else:
        downloadToFile(url,fn)

def downloadLists(urlLst,fnLst):
    assert len(urlLst)==len(fnLst)
    for i in range(len(urlLst)):
        print('\n\n'+'#'*80+'\n\n'+'Downloadind video %03d of %03d:\n'%(i+1,len(urlLst)))
        sys.stdout.flush()
        downloadToFileContinuing(urlLst[i],fnLst[i])
    print('\n\n'+'#'*80+'\n\n')
    print('All videos downloaded!\n Remember: If any video is corrupted, delete it and re-run this script.')
    sys.stdout.flush()

def main():
    downfoldername='Downloads'
    downfolder='./%s/'%downfoldername
    print('Generating local URLs')
    sys.stdout.flush()
    cont=readAllFile(animeinfofilelocation)
    infoParsed=parseInfo(cont)
    fnList=readList(infoParsed[7]+'-vid-fns.txt')
    urlVid=readList(infoParsed[7]+'-vid-url.txt')
    finalLoc=[downfolder+a for a in fnList]
    if isfile(downfoldername):
        print('There\'s a file named as %s. Remove it from this folder.'%downfolder)
        return
    if not isdir(downfoldername):
        run('mkdir '+downfolder)
    #
    downloadLists(urlVid,finalLoc)
    #
    saveList(infoParsed[7]+'.txt',finalLoc)
    print('This script done its duty.')
    print('May be a folder called "%s" with your files.'%downfolder)
    print('File that hold filenames: %s'%(infoParsed[7]+'-vid-fns.txt'))
    sys.stdout.flush()
    pass

if __name__=='__main__':
    main()
