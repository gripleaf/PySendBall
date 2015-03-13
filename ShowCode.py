#!/usr/bin/env python
#--coding = UTF-8--
import urllib2, urllib

"""
catch the code
"""

def ShowCode(path="http://10.7.18.82/JudgeOnline/showsource?solution_id=50115"):
    return  urllib2.urlopen(path).read()

if __name__ == '__main__':
    print ShowCode()