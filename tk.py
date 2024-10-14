import tkinter
from tkinter import ttk
import tkinter.messagebox

from connection import *
from functions import *
from columns import *

win = tkinter.Tk()

NB = ttk.Notebook()


################################################3

menu1 = tkinter.Menu(win)
menu2 = tkinter.Menu(menu1,tearoff=0)





#дОБАВИТЬ
menu3 = tkinter.Menu(menu2,tearoff=0)

##############################Изменить
menu4 = tkinter.Menu(menu2,tearoff=0)

########################################################Удалить
menu5 = tkinter.Menu(menu2,tearoff=0)

############################################################


######################################################

Frame1 = ttk.Frame(NB)
Frame2 = ttk.Frame(NB)
Frame3 = ttk.Frame(NB)




tree1=ttk.Treeview(Frame1,columns=acter_colums,show="headings")
tree2=ttk.Treeview(Frame2,columns=spekakl_colums,show="headings")
tree3=ttk.Treeview(Frame3,columns=bizz_acter_colums,show="headings")
###################################################################################
