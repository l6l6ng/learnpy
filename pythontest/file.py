# try:
#     f = open('./1.py', 'r')
#     s = f.read()
#     print(s)
# finally:
#     if f:
#         f.close()

# with open('./1.py', 'r') as f:
#     # f.read()
#     for line in f.readlines():
#         print(line.strip())
#
# from tkinter import *

from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()