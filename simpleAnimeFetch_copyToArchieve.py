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

def run(cmd):
    return system('bash -c "'+cmd+'"').read()

def cp(f,p):
    run('cp '+f+' '+p)

def mkdir_ondemand(a):
    if not isdir(a):
        run('mkdir '+'./%s/'%a)

def main():
    downfoldername='Downloads'
    downfolder='./%s/'%downfoldername
    archfn='archieved'
    sys.stdout.flush()
    cont=readAllFile(animeinfofilelocation)
    infoParsed=parseInfo(cont)
    fnList=readList(infoParsed[7]+'-vid-fns.txt')
    finalLoc=[downfolder+a for a in fnList]
    aafn=archfn+'/'+infoParsed[7]
    adafn=aafn+'/'+downfoldername
    mkdir_ondemand(archfn)
    mkdir_ondemand(aafn)
    mkdir_ondemand(adafn)
    print('Starting file movimentation...')
    sys.stdout.flush()
    cp('animeInfo.txt',aafn)
    cp(infoParsed[7]+'.txt',aafn)
    cp(infoParsed[7]+'-pag-url.txt',aafn)
    cp(infoParsed[7]+'-vid-url.txt',aafn)
    cp(infoParsed[7]+'-vid-fns.txt',aafn)
    [cp(f,adafn) for f in finalLoc]
    print('This script done its duty.')
    sys.stdout.flush()
    pass

if __name__=='__main__':
    main()
