#!/usr/bin/env ptyhon
#!-*- coding:utf-8 -*-
#!@Authoer:gaolanfang
import os
import sys
import getopt
import re
from string import punctuation as enpn
from zhon.hanzi import punctuation as cnpn


def main():
    # 使用方法python mmsegdict.py -f dict.txt -n newdict.txt
    inFile = ''
    outFile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:n:")
    except getopt.GetoptError:
        help()
        sys.exit()

    for op, value in opts:
        if op == "-f":
            inFile = value
        elif op == "-n":
            outFile = value
        elif op == '-h':
            help()
            sys.exit()

    if inFile == "" or outFile == "":
        help()
        sys.exit()
    elif os.path.exists(inFile) is False:
        print inFile + ' file does not exit !!!'
        sys.exit()
    else:
        createDict(inFile, outFile)


def special(str):
    line = re.sub(ur"[%s]+" % cnpn, "", str)
    out = re.sub(r"[%s]" % enpn, "", line)
    num = re.sub(r"\d", "", out)
    english = re.sub(r"[a-zA-Z]+", "", num)
    return english


def createDict(inFile, outFile):
    tempList = []
    setList = []
    content = ""
    with open(inFile, "rb") as fp:
        for line in fp.readlines():
            line = line.decode('utf-8')
            word = line.strip()
            word = special(word)
            word = word.strip()
            if word not in setList:
                setList.append(word)
            else:
                continue
            content = word + "\t1\nx:1\n"
            tempList.append(content)

    with open(outFile, "w") as f:
        for li in tempList:
            f.write(li.encode('utf-8'))


def help():
    print "mmsegdict.py -f <inputfile> -n <outputfile>"

if __name__ == '__main__':
    main()
