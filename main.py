from functions import *
from connection import *
from tk import *

#acter_colums =  ('COD_A', 'F', 'I', 'O', 'Z', 'Stag')
#spekakl_colums = ('COD_S', 'name', 'year_name', 'cost')
#bizz_acter_colums = ('COD_A', 'COD_S', 'ROL', 'cost_yesr_contr')



table1 = """--sql
CREATE TABLE IF NOT EXISTS acter(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    F text NOT NULL,
    I text NOT NULL,
    O text NOT NULL,
    Z text,
    Stag INTEGER
);
"""

table2 = """--sql
CREATE TABLE IF NOT EXISTS spekakl(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    names text NOT NULL,
    year_name INTEGER NOT NULL,
    cost INTEGER
);
"""

table3 = """--sql
CREATE TABLE IF NOT EXISTS bizz_acter(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_a INTEGER,
    id_c INTEGER,
    rol text,
    cost_year_c INTEGER,
    FOREIGN KEY (id_a) REFERENCES acter (id),
    FOREIGN KEY (id_c) REFERENCES spekakl (id)

);
"""

cursor.execute(table1)
cursor.execute(table2)
cursor.execute(table3)

#####################################################################

win.title("Практика")
win.geometry("650x650")

NB.pack(expand=True,fill="both")

win.config(menu=menu1)

menu1.add_cascade(label="Действия",menu=menu2)

menu3.add_command(label="Актеры",command=add_A)
menu3.add_command(label="Спектакли",command=add_S)
menu3.add_command(label="Занятость актеров в спектакле",command=add_Z)

menu4.add_command(label="Актеры",command=edit_A)
menu4.add_command(label="Спектакли",command=edit_S)
menu4.add_command(label="Занятость актеров в спектакле",command=edit_Z)

menu5.add_command(label="Актеры",command=del_A)
menu5.add_command(label="Спектакли",command=del_S)
menu5.add_command(label="Занятость актеров в спектакле",command=del_Z)

menu2.add_cascade(label="Добавить", menu=menu3)
menu2.add_cascade(label="Изменить",menu=menu4)
menu2.add_cascade(label="Удалить",menu=menu5)

Frame1.pack(fill="both",expand=True)
Frame2.pack(fill="both",expand=True)
Frame3.pack(fill="both",expand=True)

NB.add(Frame1,text="Актеры")
NB.add(Frame2,text="Спектакли")
NB.add(Frame3,text="Занятость актеров в спектакле")

tree1.heading(acter_colums[0],text=acter_colums[0])
tree1.heading(acter_colums[1],text=acter_colums[1])
tree1.heading(acter_colums[2],text=acter_colums[2])
tree1.heading(acter_colums[3],text=acter_colums[3])
tree1.heading(acter_colums[4],text=acter_colums[4])
tree1.heading(acter_colums[5],text=acter_colums[5])

tree2.heading(spekakl_colums[0],text=spekakl_colums[0])
tree2.heading(spekakl_colums[1],text=spekakl_colums[1])
tree2.heading(spekakl_colums[2],text=spekakl_colums[2])
tree2.heading(spekakl_colums[3],text=spekakl_colums[3])

tree3.heading(bizz_acter_colums[0],text=bizz_acter_colums[0])
tree3.heading(bizz_acter_colums[1],text=bizz_acter_colums[1])
tree3.heading(bizz_acter_colums[2],text=bizz_acter_colums[2])
tree3.heading(bizz_acter_colums[3],text=bizz_acter_colums[3])
tree3.heading(bizz_acter_colums[4],text=bizz_acter_colums[4])
###########################################################################################Показали вверх табилцы
tree2.pack(expand=True,fill="both")
tree1.pack(expand=True,fill="both")
tree3.pack(expand=True,fill="both")



ent_scr = tkinter.Entry(win,width=20)
btn_scr = ttk.Button(win,text="Найти", command=lambda:def_scr(ent_scr))

ent_scr.pack(anchor="s")
btn_scr.pack(anchor="s")


NB.bind("<<NotebookTabChanged>>" , tab_change)

for value_acter in add_data_on_interface_acter:
    
    tree1.insert("", "end", values=value_acter)


for value_spekakl in add_data_on_interface_spekakl:
    tree2.insert("","end",values=value_spekakl)

for value_bizz_act in add_data_on_interface_bizz_acter:
    tree3.insert("","end",values=value_bizz_act)



win.mainloop()
