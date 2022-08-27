import tkinter as tk

from tkinter import ANCHOR, CENTER, ttk, Canvas
from PIL import Image, ImageTk

root = tk.Tk()

class Globals():
    appname = "Image Tester"
    icon = "tools.png"
    author = "Some Person"
    contact = "someperson@gmail.com"
    codeassist = "Another Person"
    git = "https://github.com/someperson/test.git"

class Actions():
    def exitapp():
        root.quit()

    def openhelp():
        helpwindow = tk.Toplevel(root)
        helpwindow.title(Globals.appname)
        ico = Image.open(Globals.icon)
        photo = ImageTk.PhotoImage(ico)
        helpwindow.wm_iconphoto(False, photo)
        helpwinttlfrm = tk.LabelFrame(helpwindow, text = "Help")
        helpwinttlfrm.grid(column = 0, row = 0, padx = 5, pady = 5, sticky="NSEW")
        helpauthorlbl = tk.Label(helpwinttlfrm, text ="Test Label")
        helpauthorlbl.grid(column= 0, row = 0, padx = 5, pady = 5, sticky="W")

    def openabout():
        aboutwindow = tk.Toplevel(root)
        aboutwindow.title(Globals.appname)
        ico = Image.open(Globals.icon)
        photo = ImageTk.PhotoImage(ico)
        aboutwindow.wm_iconphoto(False, photo)
        aboutwinttlfrm = tk.LabelFrame(aboutwindow, text = "About")
        aboutwinttlfrm.grid(column = 0, row = 0, padx = 5, pady = 5, sticky="NSEW")
        #img = Image.open(Globals.icon)
        #img.resize((64, 64))
        image = ImageTk.PhotoImage(ico.resize((127, 127)))
        aboutcanvas = Canvas(aboutwinttlfrm, width=128, height=128)
        aboutcanvas.grid(column=0, row=0, padx = 5, pady = 5, sticky="W")
        aboutcanvas.create_image(64, 64, image = image)
        aboutttllbl = tk.Label(aboutwinttlfrm, text=Globals.appname)
        aboutttllbl.grid(column=1, row=0, padx = 5, pady = 5, sticky="SW")
        aboutauthorlbl = tk.Label(aboutwinttlfrm, text ="Written By:")
        aboutauthorlbl.grid(column = 0, row = 1, padx = 5, pady = 5, sticky="W")
        aboutauthor = tk.Label(aboutwinttlfrm, text = Globals.author)
        aboutauthor.grid(column = 1, row = 1, padx = 5, pady = 5, sticky="W")
        aboutcontactlbl = tk.Label(aboutwinttlfrm, text ="Contact:")
        aboutcontactlbl.grid(column = 0, row = 2, padx = 5, pady = 5, sticky="W")
        aboutcontact = tk.Label(aboutwinttlfrm, text = Globals.contact)
        aboutcontact.grid(column = 1, row = 2, padx = 5, pady = 5, sticky="W")
        aboutcodeasstlbl = tk.Label(aboutwinttlfrm, text ="Coding Assistance:")
        aboutcodeasstlbl.grid(column = 0, row = 3, padx = 5, pady = 5, sticky="W")
        aboutcodeasst = tk.Label(aboutwinttlfrm, text = Globals.codeassist)
        aboutcodeasst.grid(column = 1, row = 3, padx = 5, pady = 5, sticky="W")
        aboutgitlbl = tk.Label(aboutwinttlfrm, text ="Git Link:")
        aboutgitlbl.grid(column = 0, row = 4, padx = 5, pady = 5, sticky="W")
        aboutgithubgit = tk.Label(aboutwinttlfrm, text = Globals.git)
        aboutgithubgit.grid(column = 1, row = 4, padx = 5, pady = 5, sticky="W")
        aboutverlbl = tk.Label(aboutwinttlfrm, text = "Version:")
        aboutverlbl.grid(column = 0, row = 5, padx = 5, pady = 5, sticky="W")
        aboutver = tk.Label(aboutwinttlfrm, text = Globals.ver)
        aboutver.grid(column = 1, row = 5, padx = 5, pady = 5, sticky="W")

class App():
    root.title(Globals.appname)
    root.geometry("260x210")
    ico = Image.open(Globals.icon)
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    nb = ttk.Notebook(root)
    menubar = tk.Menu(nb)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=Actions.exitapp)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = tk.Menu(menubar, tearoff=0)                                     
    helpmenu.add_command(label="Help", command=Actions.openhelp)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=Actions.openabout)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
    root.mainloop()
    
app=App()
