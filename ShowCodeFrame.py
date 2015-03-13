__author__ = 'glcsnz123'
import wx;
import wx.html
import urllib, urllib2
from Login import Login
from ShowCode import ShowCode
import re

class ShowCodeFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=-1, title="ShowTheCode", size=(800, 700), pos=(300, 100))
        #self.panel = wx.Panel(self, -1);
        #Login();
        #self.Show(True)
        self.html = wx.html.HtmlWindow(self, -1)
        self.code_list = []

        #create the static text
        wx.StaticText(self.html, -1, "     User ID:", pos=(40, 20))
        wx.StaticText(self.html, -1, "Problem ID:", pos=(250, 20))

        #create the text ctrl
        self.user_id = wx.TextCtrl(self.html, -1, pos=(120, 17), value="10600140")
        self.pro_id = wx.TextCtrl(self.html, -1, pos=(330, 17), value="2010")

        #create the button
        self.Search = wx.Button(self.html, -1, "Search", pos=(450, 15))

        #create the bind
        self.Bind(wx.EVT_BUTTON, self.ShowCodeLine, self.Search)

        self.Show(True);

    def CreateCodeList(self):
        #create choice
        wx.StaticText(self.html, -1, "Chose the problem:", pos=(100, 70))
        self.codepro = wx.Choice(self.html, id=-1, pos=(245, 68), choices=self.pro_list)
        #codeurl = wx.Choice(self.html, id=-1, pos=(200, 60), choices=self.url_list)

        self.Bind(wx.EVT_CHOICE, self.HtmlShow, self.codepro)

    def ShowCodeLine(self, event):
        #post_data = urllib.urlencode({"problem_id": self.pro_id.GetValue(), "user_id": self.user_id.GetValue()})
        url = r"http://10.7.18.82/JudgeOnline/status?"
        if self.pro_id.GetValue() != "":
            url = url + "problem_id=" + self.pro_id.GetValue()
        if self.user_id.GetValue != "":
            url = url + "user_id=" + self.user_id.GetValue()
        url = url + r"&result=0"

        htmlt = urllib2.urlopen(url).read()
        #self.html.SetPage(htmlt)
        reg = re.compile("showsource\?solution_id=[0-9]+")
        self.url_list = reg.findall(htmlt)
        self.pro_list = re.compile(r"showproblem\?problem_id=....").findall(htmlt)
        self.code_list = []
        for i in range(0, len(self.pro_list)):
            self.pro_list[i] = self.pro_list[i][len(self.pro_list[i]) - 4:]
            self.code_list.append((self.pro_list[i], self.url_list))

        #create the codelist
        self.CreateCodeList()

    def HtmlShow(self, event):
        self.html.SetStandardFonts()
        #print self.url_list[self.codepro.GetSelection()] + "****"
        self.html.SetPage(r"<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>" + ShowCode(\
            "http://10.7.18.82/JudgeOnline/" + self.url_list[self.codepro.GetSelection()]))


if __name__ == '__main__':
    Login()
    app = wx.PySimpleApp();
    frame = ShowCodeFrame(None)
    frame.Show(True)
    app.MainLoop()
