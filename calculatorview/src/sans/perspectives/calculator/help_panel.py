#!/usr/bin/python
"""
Help panel for calculator
"""
import os
import wx
import wx.html as html
from wx.lib.splitter import MultiSplitterWindow
import sans.perspectives.calculator as calculator


class HelpWindow(wx.Frame):
    """
    """
    def __init__(self, parent, title="Tool Help", pageToOpen=None):
        wx.Frame.__init__(self, parent, title, size=(700, 450))
        """
             contains help info
        """
        self.SetTitle("Tool Help",) 
        splitter = MultiSplitterWindow(self, style=wx.SP_LIVE_UPDATE)
        rpanel = wx.Panel(splitter, -1)
        lpanel = wx.Panel(splitter, -1, style=wx.BORDER_SUNKEN)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        header = wx.Panel(rpanel, -1)
        header.SetBackgroundColour('#6666FF')
        header.SetForegroundColour('WHITE')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        st = wx.StaticText(header, -1, 'Contents', (5, 5))
        font = st.GetFont()
        font.SetPointSize(10)
        st.SetFont(font)
        hbox.Add(st, 1, wx.TOP | wx.BOTTOM | wx.LEFT, 5)
        header.SetSizer(hbox)
        vbox.Add(header, 0, wx.EXPAND)
       
        vboxl = wx.BoxSizer(wx.VERTICAL)
        headerl = wx.Panel(lpanel, -1, size=(-1, 20))
       
        headerl.SetBackgroundColour('#6666FF')
        headerl.SetForegroundColour('WHITE')
        hboxl = wx.BoxSizer(wx.HORIZONTAL)
        lst = wx.StaticText(headerl, -1, 'Menu', (5, 5))
        fontl = lst.GetFont()
        fontl.SetPointSize(10)
        lst.SetFont(fontl)
        hboxl.Add(lst, 1, wx.TOP | wx.BOTTOM | wx.LEFT, 5)
        headerl.SetSizer(hboxl)
        vboxl.Add(headerl, 0, wx.EXPAND)
        self.lhelp = html.HtmlWindow(lpanel, -1, style=wx.NO_BORDER)
        self.rhelp = html.HtmlWindow(rpanel, -1, style=wx.NO_BORDER, 
                                     size=(500,-1))
        
        self.path = calculator.get_data_path(media='media')
       
        page1 = """<html>
            <body>
             <p>Select topic on Menu</p>
            </body>
            </html>"""
        self.rhelp.SetPage(page1)
        page = """<html>
            <body>
            <ul>
            <li><a href ="data_operator_help.html" 
            target ="showframe">Data Operator</a><br></li>
            <li><a href ="sld_calculator_help.html" 
            target ="showframe">SLD Calculator</a><br></li>
            <li><a href ="density_calculator_help.html" 
            target ="showframe">Density Calculator</a><br></li>
            <li><a href ="slit_calculator_help.html" 
            target ="showframe">Slit Size Calculator</a><br></li>
            <li><a href ="kiessig_calculator_help.html" 
            target ="showframe">Kiessig Thickness Calculator</a><br></li>
            <li><a href ="resolution_calculator_help.html" 
            target ="showframe">Resolution Estimator</a><br></li>
            <li><a href ="pycrust_help.html" 
            target ="showframe">Python Shell</a><br></li>
            </ul>
            </body>
            </html>"""

        self.lhelp.SetPage(page)
        self.lhelp.Bind(wx.html.EVT_HTML_LINK_CLICKED, self.OnLinkClicked)
        
        vbox.Add(self.rhelp, 1, wx.EXPAND)
        vboxl.Add(self.lhelp, 1, wx.EXPAND)
        rpanel.SetSizer(vbox)
        lpanel.SetSizer(vboxl)
        lpanel.SetFocus()
        
        vbox1 = wx.BoxSizer(wx.HORIZONTAL)
        vbox1.Add(splitter, 1, wx.EXPAND)
        splitter.AppendWindow(lpanel, 200)
        splitter.AppendWindow(rpanel)
        self.SetSizer(vbox1)
       
        self.Centre()
        self.Show(True)
        
    def OnLinkClicked(self, event):
        """
            Function to diplay html page related to the hyperlinktext selected
        """
        link = event.GetLinkInfo().GetHref()
        link = os.path.join(self.path, link)
        self.rhelp.LoadPage(link)
        
        
class ViewApp(wx.App):
    def OnInit(self):
        frame = HelpWindow(None, -1, 'HelpWindow')    
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
        
if __name__ == "__main__": 
    app = ViewApp(0)
    app.MainLoop()     
