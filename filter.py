#!/usr/bin/env python
# _*_coding:utf-8 _*_
#Time : 2019/9/4 14:55
#Author : glf
#by : PyCharm

import codecs
import argparse

def main(file, length, newFile):
    content = []
    with codecs.open(file, 'r', encoding='UTF-8') as fp:
        for line in fp.readlines():
            word = line.strip()
            if int(len(word)) < int(length):
                content.append(word)

    with codecs.open(newFile, 'w', encoding='UTF-8') as f:
        for list in content:
            f.writelines(list + '\n')


if __name__ == '__main__':
    argParser = argparse.ArgumentParser(description=u'把文件中指定长度的中文删除')
    argParser.add_argument('-a', dest='file', required=True, help=u'文件的路径')
    argParser.add_argument('-l', dest='length', required=True, help=u'长度')
    argParser.add_argument('-o', dest='output', required=True, help=u'输出文件的路径')
    args = argParser.parse_args()

    main(args.file, args.length, args.output)