#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:31:43 2015

@author: adler
"""

import sys
from os import popen as system
from time import sleep as timedpause

animeinfofilelocation='animeInfo.txt'

wgetUserAgent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'

def urlAssembler(infoParsed):
    base=''.join(infoParsed[0]+infoParsed[1]+infoParsed[5])
    return [(base%k)+infoParsed[8] for k in range(infoParsed[2],infoParsed[3]+1)]

def fileNameAssembler(infoParsed):
    base=''.join(infoParsed[4]+infoParsed[5])
    return [(base%k)+infoParsed[6] for k in range(infoParsed[2],infoParsed[3]+1)]

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
    tpause=3
    run('wget -U \''+wgetUserAgent+'\' '+url+' -O tmpfile.tmp')
    a=readAllFile('tmpfile.tmp')
    run('rm tmpfile.tmp')
    print("\nPlease wait %.2f seconds to avoid flooding the server...\n\n\n"%(tpause)+'#'*80+'\n')
    sys.stdout.flush()
    timedpause(tpause) #Avoid being caught by the anti-flood system.
    return a

def superanimesParser(urllist):
    l=[]
    for url in range(len(urllist)):
        print('Downloading HTML %03d of %03d...'%(url+1,len(urllist)))
        sys.stdout.flush()
        page=download(urllist[url])
        page=page.split('<video')[1].split('<source src="')[1].split('"')[0]
        l.append(page)
    print('All HTMLs downloaded!')
    return l

def main():
    print('Generating local URLs')
    sys.stdout.flush()
    cont=readAllFile(animeinfofilelocation)
    infoParsed=parseInfo(cont)
    fnList=fileNameAssembler(infoParsed)
    urlList=urlAssembler(infoParsed)
    print('Saving files...')
    sys.stdout.flush()
    saveList(infoParsed[7]+'-vid-fns.txt',fnList)
    saveList(infoParsed[7]+'-pag-url.txt',urlList)
    print('Downloading video links...')
    sys.stdout.flush()
    urlVid=superanimesParser(urlList)
    print('Saving video links in a list...')
    sys.stdout.flush()
    saveList(infoParsed[7]+'-vid-url.txt',urlVid)
    print('This script done its duty. There\'s another script for downloading the videos.')
    sys.stdout.flush()
    pass

if __name__=='__main__':
    main()
