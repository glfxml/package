#!/usr/bin/env ptyhon
#!-*- coding:utf-8 -*-
#!@Authoer:gaolanfang
import os
import sys
import getopt

def main():

	#使用方法python mmsegdict.py -f dict.txt -n newdict.txt
	inFile = ''
	outFile = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hf:n:")
	except getopt.GetoptError:
		help()
		sys.exit()

	for op,value in opts:
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
	elif os.path.exists(inFile) == False:
		print inFile + ' file does not exit !!!'
		sys.exit()
	else:
		createDict(inFile, outFile)

def createDict(inFile, outFile):
	tempList = []
	content = ""
	with open(inFile, "r") as fp:
		for line in fp.readlines():
			content = line.strip() + "\t1\nx:1\n"
			tempList.append(content)

	
	with open(outFile, "w") as f:
		for li in tempList:
			f.write(li)



def help():
	print "mmsegdict.py -f <inputfile> -n <outputfile>"


if __name__ == '__main__':
	main()