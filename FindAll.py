__author__ = 'glcsnz123'
import re;
import urllib
import sys, urllib2
import cookielib
from Login import Login

def format_user(username):
    return username.replace(r"userstatus?user_id=", "")



def FindAll(path="http://10.7.18.82/JudgeOnline/status?contest_id=1136&result=0"):
    source = urllib2.urlopen(path)
    htmlt = source.read();

    print htmlt;
    # find the user
    re_useg = re.compile(r'userstatus\?user_id=.{1,15}>')
    user_data = map(format_user, re_useg.findall(htmlt))

    #find the result
    re_rseg = re.compile(r'showproblem\?problem_id=....>[A-Z]')
    result_data = re_rseg.findall(htmlt)

    #find the codenumber
    re_cseg = re.compile(r'showsource\?solution_id=[0-9]+')
    code_data = re_cseg.findall(htmlt)

    #print code_data;
    #print user_data;

    user_resu = [];

    for i in range(0, len(user_data)):
        if len(code_data) == 0:
            user_resu.append((user_data[i][:-1], result_data[i][-1], 0))
        else:
            user_resu.append((user_data[i][:-1], result_data[i][-1], code_data[i]))
    return user_resu;

if __name__ == '__main__':
    FindAll("http://10.7.18.82/JudgeOnline/status?problem_id=2010&user_id=10600140&result=0")
