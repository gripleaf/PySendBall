#!/usr/bin/env python
#--coding = UTF-8--
import sys, urllib2, urllib
import cookielib
from ShowCode import ShowCode

def Login(user="longpo", passwd="longpo123", path=r"http://10.7.18.82/JudgeOnline/login?action=login"):
    try:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent', 'Opera/9.23')]

        post_data = urllib.urlencode({"user_id1": user, "password1": passwd});
        urllib2.install_opener(opener)
        req = urllib2.Request(path, post_data)
        conn = urllib2.urlopen(req)
        htmlc = conn.read();
        #print urllib2.urlopen("http://10.7.18.82/JudgeOnline/showsource?solution_id=50115").read()
        #print ShowCode();

        if htmlc.find("Welcome") == -1:
            return 0
        else: print "Login success!"
        return 1

    except Exception, ex:
        return 0

if __name__ == '__main__':
    Login();