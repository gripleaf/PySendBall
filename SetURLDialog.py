__author__ = 'glcsnz123'
import wx;

class SetURLDialog(wx.TextEntryDialog):
    def __init__(self, parent):
        wx.TextEntryDialog.__init__(self, parent, caption="Set The URL", message="Input the URL:")
        self.Show(True)




