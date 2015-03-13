#!/usr/bin/env python
#--coding = UTF-8--
__author__ = 'glcsnz123'
from Login import Login
from ShowCode import ShowCode
from Login_Input import Login_Input
from ShowCodeFrame import ShowCodeFrame
from SetURLDialog import SetURLDialog
import wx

class SendFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=-1, title="SendBall", size=(600, 600),style=wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP)
        self.panel = wx.Panel(self, -1);
        self.panel.SetBackgroundColour("white")

        #create menuBar and statusBar
        self.CreateTheMenuBar()
        self.CreateStatusBar()

    def LoginIn(self, event):
        Login_Input(self)

    def ShowTheCode(self, event):
        ShowCodeFrame(self)

    def SetURL(self, event):
        url_dialog = SetURLDialog(self)
        if url_dialog.ShowModal() == wx.OK:
            self.url = url_dialog.GetValue()


    def CreateTheMenuBar(self):
        menuBar = wx.MenuBar();

        #create menu
        menu1 = wx.Menu()

        #create menuItem
        mIU = menu1.Append(-1, "Set URL",\
            "Set the Url.Remember, you just show the ID like this 'http://10.7.18.82/JudgeOnline/status?contest_id=1138&result=0'")
        mIL = menu1.Append(-1, "Login", "Login in the web")
        mIS = menu1.Append(-1, "ShowTheCode", "Show the code you want")

        #Append
        menuBar.Append(menu1, "&File")
        self.SetMenuBar(menuBar)

        #create the bind
        self.Bind(wx.EVT_MENU, self.LoginIn, mIL)
        self.Bind(wx.EVT_MENU, self.ShowTheCode, mIS)
        self.Bind(wx.EVT_MENU, self.SetURL, mIU)


if __name__ == '__main__':#main function
    app = wx.PySimpleApp();
    frame = SendFrame();
    frame.Show(True);
    app.MainLoop()






