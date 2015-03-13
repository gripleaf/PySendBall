import wx
from Login import Login

"""
    login frame
    finish login
"""

class Login_Input(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=-1, title="Login Dialog", size=(275, 264))
        panel = wx.Panel(self, id=-1);
        panel.SetBackgroundColour("white")
        self.Show(True)
        #create label
        wx.StaticText(panel, id=-1, label="Username:", pos=(30, 40))
        wx.StaticText(panel, id=-1, label="Password:", pos=(32, 80))
        self.st_warn = wx.StaticText(panel, id=-1, label="", pos=(90, 150))
        self.st_warn.SetBackgroundColour("red")


        #create textField
        self.user = wx.TextCtrl(panel, id=-1, value="", pos=(100, 40))
        self.urpasswd = wx.TextCtrl(panel, id=-1, value="", pos=(100, 80), style=wx.TE_PASSWORD)

        #create Button
        but_login = wx.Button(panel, id=-1, label="Login", pos=(40, 120))
        but_cancel = wx.Button(panel, label="Cancel", pos=(140, 120));

        #create Bind
        self.Bind(wx.EVT_BUTTON, self.LoginHandler, but_login)
        self.Bind(wx.EVT_BUTTON, self.OnClose, but_cancel)


    def LoginHandler(self, event):
        if Login(self.user.GetValue(), self.urpasswd.GetValue()) == 1:
            self.Destroy();
        else:
            self.st_warn.SetLabel("wrong!!")

    def OnClose(self, event):
        self.Destroy()
