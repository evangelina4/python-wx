#创建一个文本编辑器
import wx
app = wx.App()
win = wx.Frame(None,title = '编辑器',size = (410,335))
win.Show()

loadButton = wx.Button(win,label = 'open',pos = (225,5),size = (80,25))
saveButton = wx.Button(win,label = 'save',pos = (315,5),size = (80,25))
filename = wx.TextCtrl(win,pos = (5,5),size = (210,25))
contents = wx.TextCtrl(win,pos = (5,35),size = (390,260),style = wx.TE_MULTILINE | wx.HSCROLL)
app.MainLoop()
#wx.TE_MULTILINE来获取多行文件区,wx.HSCROLL来获取水平滚动条
