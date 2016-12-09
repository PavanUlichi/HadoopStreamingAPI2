#!/usr/bin/python

import sys
import ast
#executes till there is an input line from STDIN
for line in sys.stdin:
        #taking each line to a variable one by one
        line = line.strip()
        #taking each word in the line, separated by tab space to a variable "words"
        words=line.split('\t')
        data = ast.literal_eval(words[04])
        try:
                p = data["subjects"]
        except KeyError:
                p = ""
                pass
        for q in p: 
                print "%s\t\t%s" %(q,1)
