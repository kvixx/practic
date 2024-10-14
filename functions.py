import tkinter
from tkinter import ttk
import tkinter.messagebox

from tk import *
from connection import *
from columns import *

add_data_on_interface_acter=con.execute("""--sql
SELECT * FROM acter
""")

add_data_on_interface_spekakl = con.execute("""--sql
SELECT * FROM spekakl
""")

add_data_on_interface_bizz_acter = con.execute("""--sql
SELECT * FROM bizz_acter
""")

######################
############################################################Добавление##########################
def cliked_add_A(window,ent2,ent3,ent4,ent5,ent6):
    value_ent2 = ent2.get()
    value_ent3 = ent3.get()
    value_ent4 = ent4.get()
    value_ent5 = ent5.get()
    value_ent6 = ent6.get()
    
    value = (value_ent2,value_ent3,value_ent4,value_ent5,value_ent6)

    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()


    curs.execute("""--sql
    INSERT INTO acter (F,I,O,Z,Stag) VALUES(?,?,?,?,?)
    """,value)

    for item in tree1.get_children():
        tree1.delete(item)

    add_data_on_interface_acter=conn.execute("""--sql
    SELECT * FROM acter
    """)
    

    for value_acter in add_data_on_interface_acter:
        tree1.insert("","end",values=value_acter)

    
    conn.commit()
    window.destroy()


def add_A():
    win1 = tkinter.Tk()
    win1.title("Добавить:Актер")
    win1.geometry('350x350')
    
    label2 = tkinter.Label(win1,text="Фамилия")
    label3 = tkinter.Label(win1,text="Имя")
    label4 = tkinter.Label(win1,text="Отчество")
    label5 = tkinter.Label(win1,text="Звание")
    label6 = tkinter.Label(win1,text="Стаж")

    
    ent2 =tkinter.Entry(win1,width=20)
    ent3 =tkinter.Entry(win1,width=20)
    ent4 =tkinter.Entry(win1,width=20)
    ent5 =tkinter.Entry(win1,width=20)
    ent6 =tkinter.Entry(win1,width=20)

    
    label2.grid(row=0,column=0)
    label3.grid(row=1,column=0)
    label4.grid(row=2,column=0)
    label5.grid(row=3,column=0)
    label6.grid(row=4,column=0)

    
    ent2.grid(row=0,column=1)
    ent3.grid(row=1,column=1)
    ent4.grid(row=2,column=1)
    ent5.grid(row=3,column=1)
    ent6.grid(row=4,column=1)

    btn = ttk.Button(win1,text="SAVE",command=lambda: cliked_add_A(win1,ent2,ent3,ent4,ent5,ent6))

    btn.grid(row=5,column=2)
##############################################################################################################

def cliked_add_S(window,ent2,ent3,ent4):
    value_ent2 = ent2.get()
    value_ent3 = ent3.get()
    value_ent4 = ent4.get()
    
    value = (value_ent2,value_ent3,value_ent4)

    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()


    curs.execute("""--sql
    INSERT INTO spekakl (names,year_name,cost) VALUES(?,?,?)
    """,value)

    for item in tree2.get_children():
        tree2.delete(item)

    add_data_on_interface_spekakl=conn.execute("""--sql
    SELECT * FROM spekakl
    """)
    

    for value_spekakl in add_data_on_interface_spekakl:
        tree2.insert("","end",values=value_spekakl)

    
    conn.commit()
    window.destroy()

def add_S():
    win1 = tkinter.Tk()
    win1.title("Добавить:Спектакли")
    win1.geometry('350x350')

    label2 = tkinter.Label(win1,text="Название")
    label3 = tkinter.Label(win1,text="Год постановки")
    label4 = tkinter.Label(win1,text="Бюджет")

    ent2 = tkinter.Entry(win1,width=20)
    ent3 = tkinter.Entry(win1,width=20)
    ent4 = tkinter.Entry(win1,width=20)

    label2.grid(row=0,column=0)
    label3.grid(row=1,column=0)
    label4.grid(row=2,column=0)

    ent2.grid(row=0,column=1)
    ent3.grid(row=1,column=1)
    ent4.grid(row=2,column=1)

    btn = ttk.Button(win1,text="SAVE",command=lambda: cliked_add_S(win1,ent2,ent3,ent4))

    btn.grid(row=3,column=2)

###########################################################################
def cliked_add_Z(window,ent1,ent2,ent3,ent4):

    ent1_v = ent1.get()
    ent2_v = ent2.get()
    ent3_v = ent3.get()
    ent4_v = ent4.get()
    value = (ent1_v,ent2_v,ent3_v,ent4_v)

    conn =sqlite3.connect("DATABASS.db")

    curs = conn.cursor()

    curs.execute("""--sql
    INSERT INTO bizz_acter (id_a,id_c,rol,cost_year_c) VALUES(?,?,?,?)
    """,value)

    for item in tree3.get_children():
        tree3.delete(item)

    add_data_on_interface_bizz_acter=conn.execute("""--sql
    SELECT * FROM bizz_acter
    """)
    

    for value_bizz_acter in add_data_on_interface_bizz_acter:
        tree3.insert("","end",values=value_bizz_acter)

    conn.commit()
    window.destroy()



def add_Z():
    win1 = tkinter.Tk()
    win1.title("Добавить:Занятость актеров в спектакле")
    win1.geometry("350x350")

    label1 = tkinter.Label(win1,text="Код актёра")
    label2 = tkinter.Label(win1,text="Код спектакля")
    label3 = tkinter.Label(win1,text="Роль")
    label4 = tkinter.Label(win1,text="Цена за год")

    ent1 = tkinter.Entry(win1,width=20)
    ent2 = tkinter.Entry(win1,width=20)
    ent3 = tkinter.Entry(win1,width=20)
    ent4 = tkinter.Entry(win1,width=20)

    label1.grid(row=0,column=0)
    label2.grid(row=1,column=0)
    label3.grid(row=2,column=0)
    label4.grid(row=3,column=0)

    ent1.grid(row=0,column=1)
    ent2.grid(row=1,column=1)
    ent3.grid(row=2,column=1)
    ent4.grid(row=3,column=1)

    btn1 = ttk.Button(win1,text="SAVE",command=lambda:cliked_add_Z(win1,ent1,ent2,ent3,ent4))

    btn1.grid(row=4,column=2)


################################################################Изменения##########################
def cliked_edit_A(window,ent_id,ent2,ent3,ent4,ent5,ent6):
    rec_id = ent_id.get()
    value_ent2 = ent2.get()
    value_ent3 = ent3.get()
    value_ent4 = ent4.get()
    value_ent5 = ent5.get()
    value_ent6 = ent6.get()

    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()

    curs.execute("""--sql
    UPDATE acter 
    SET F = ?, I = ?, O = ?, Z = ?, Stag = ? 
    WHERE id = ?  -- Замените 'id' на имя вашего столбца идентификатора
    """, (value_ent2, value_ent3, value_ent4, value_ent5, value_ent6, rec_id))

    for item in tree1.get_children():
        tree1.delete(item)

    add_data_on_interface_acter = conn.execute("""--sql
    SELECT * FROM acter
    """)

    for value_acter in add_data_on_interface_acter:
        tree1.insert("", "end", values=value_acter)
    conn.commit()
    window.destroy()


def edit_A():
    win1 = tkinter.Tk()
    win1.title("Изменить:Актер")
    win1.geometry("350x350")
    
    label_id = tkinter.Label(win1,text = "ID")
    label2 = tkinter.Label(win1,text="Фамилия")
    label3 = tkinter.Label(win1,text="Имя")
    label4 = tkinter.Label(win1,text="Отчество")
    label5 = tkinter.Label(win1,text="Звание")
    label6 = tkinter.Label(win1,text="Стаж")

    ent_id = tkinter.Entry(win1,width=20)
    ent2 =tkinter.Entry(win1,width=20)
    ent3 =tkinter.Entry(win1,width=20)
    ent4 =tkinter.Entry(win1,width=20)
    ent5 =tkinter.Entry(win1,width=20)
    ent6 =tkinter.Entry(win1,width=20)

    label_id.grid(row=0,column=0)
    label2.grid(row=2,column=0)
    label3.grid(row=3,column=0)
    label4.grid(row=4,column=0)
    label5.grid(row=5,column=0)
    label6.grid(row=6,column=0)

    ent_id.grid(row=0,column=1)
    ent2.grid(row=2,column=1)
    ent3.grid(row=3,column=1)
    ent4.grid(row=4,column=1)
    ent5.grid(row=5,column=1)
    ent6.grid(row=6,column=1)

    btn = ttk.Button(win1,text="EDIT",command=lambda: cliked_edit_A(win1,ent_id,ent2,ent3,ent4,ent5,ent6))

    btn.grid(row=7,column=2)

#################################################################################
def cliked_edit_S(window,ent_id,ent2,ent3,ent4):
    rec_id = ent_id.get()
    value_ent2 = ent2.get()
    value_ent3 = ent3.get()
    value_ent4 = ent4.get()


    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()

    curs.execute("""--sql
    UPDATE spekakl 
    SET names = ?, year_name = ?, cost = ? 
    WHERE id = ?  -- Замените 'id' на имя вашего столбца идентификатора
    """, (value_ent2, value_ent3, value_ent4, rec_id))

    for item in tree2.get_children():
        tree2.delete(item)

    add_data_on_interface_spekakl = conn.execute("""--sql
    SELECT * FROM spekakl
    """)

    for value_spekakl in add_data_on_interface_spekakl:
        tree2.insert("", "end", values=value_spekakl)
    conn.commit()
    window.destroy()

def edit_S():
    win1 = tkinter.Tk()
    win1.title("Изменить:Спектакли")
    win1.geometry('350x350')

    label_id = tkinter.Label(win1,text="ID")
    label2 = tkinter.Label(win1,text="Название")
    label3 = tkinter.Label(win1,text="Год постановки")
    label4 = tkinter.Label(win1,text="Бюджет")

    ent_id = tkinter.Entry(win1,width=20)
    ent2 = tkinter.Entry(win1,width=20)
    ent3 = tkinter.Entry(win1,width=20)
    ent4 = tkinter.Entry(win1,width=20)

    label_id.grid(row=0,column=0)
    label2.grid(row=2,column=0)
    label3.grid(row=3,column=0)
    label4.grid(row=4,column=0)

    ent_id.grid(row=0,column=1)
    ent2.grid(row=2,column=1)
    ent3.grid(row=3,column=1)
    ent4.grid(row=4,column=1)

    btn = ttk.Button(win1,text="EDIT",command=lambda: cliked_edit_S(win1,ent_id,ent2,ent3,ent4))

    btn.grid(row=5,column=2)
################################################################################
def cliked_edit_Z(window,ent_id,ent3,ent4):
    v_rec_id = ent_id.get()
    v_ent3 = ent3.get()
    v_ent4 = ent4.get()

    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()

    curs.execute("""--sql
    UPDATE bizz_acter 
    SET rol = ?, cost_year_c = ? 
    WHERE id = ?  -- Замените 'id' на имя вашего столбца идентификатора
    """, (v_ent3,v_ent4,v_rec_id))

    for item in tree3.get_children():
        tree3.delete(item)

    add_data_on_interface_bizz_acter = conn.execute("""--sql
    SELECT * FROM bizz_acter
    """)

    for value_bizz_acter in add_data_on_interface_bizz_acter:
        tree3.insert("", "end", values=value_bizz_acter)
    conn.commit()
    window.destroy()

def edit_Z():
    win1 = tkinter.Tk()
    win1.title("Изменить:Занятость актеров в спектакле")
    win1.geometry("350x350")
    label_id = tkinter.Label(win1,text="ID")
    label3 = tkinter.Label(win1,text="Роль")
    label4 = tkinter.Label(win1,text="Цена за год")

    ent_id = tkinter.Entry(win1,width=20)
    ent3 = tkinter.Entry(win1,width=20)
    ent4 = tkinter.Entry(win1,width=20)

    label_id.grid(row=0,column=0)
    label3.grid(row=1,column=0)
    label4.grid(row=2,column=0)

    ent_id.grid(row=0,column=1)
    ent3.grid(row=1,column=1)
    ent4.grid(row=2,column=1)

    btn1 = ttk.Button(win1,text="SAVE",command=lambda:cliked_edit_Z(win1,ent_id,ent3,ent4))

    btn1.grid(row=5,column=2)
#################################################################################

def cliked_del_A(window,ent1):
    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()
    rec_id = ent1.get()
    # Выполняем команду DELETE
    curs.execute("DELETE FROM acter WHERE id = ?", (rec_id,))

    # Очистка tree1 перед добавлением новых данных
    for item in tree1.get_children():
        tree1.delete(item)

    # Загрузка обновленных данных из базы данных
    add_data_on_interface_acter = conn.execute("SELECT * FROM acter")
    
    for value_acter in add_data_on_interface_acter:
        tree1.insert("", "end", values=value_acter)
    conn.commit()
    window.destroy()
    

def del_A():
    win1 = tkinter.Tk()
    win1.title("Удалить:Актер")
    win1.geometry("350x350")
    label1= tkinter.Label(win1,text="ID")
    
    ent1 = tkinter.Entry(win1,width=20)

    label1.grid(row=0,column=0)
    ent1.grid(row=0,column=1)

    btn_del = ttk.Button(win1,text="Удалить",command=lambda: cliked_del_A(win1,ent1))

    btn_del.grid(row=0,column=4)

###############################################################################
def cliked_del_S(window,ent1):
    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()
    rec_id = ent1.get()
    # Выполняем команду DELETE
    curs.execute("DELETE FROM spekakl WHERE id = ?", (rec_id,))

    # Очистка tree1 перед добавлением новых данных
    for item in tree2.get_children():
        tree2.delete(item)

    # Загрузка обновленных данных из базы данных
    add_data_on_interface_spekakl = conn.execute("SELECT * FROM spekakl")
    
    for value_spekakl in add_data_on_interface_spekakl:
        tree2.insert("", "end", values=value_spekakl)
    conn.commit()
    window.destroy()

def del_S():
    win1 = tkinter.Tk()
    win1.title("Удалить:Спектакли")
    win1.geometry("350x350")
    label1= tkinter.Label(win1,text="ID")
    
    ent1 = tkinter.Entry(win1,width=20)

    label1.grid(row=0,column=0)
    ent1.grid(row=0,column=1)

    btn_del = ttk.Button(win1,text="Удалить",command=lambda: cliked_del_S(win1,ent1))

    btn_del.grid(row=0,column=4)
###############################################################################
def cliked_del_Z(window,ent1):
    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()
    rec_id = ent1.get()
    # Выполняем команду DELETE
    curs.execute("DELETE FROM bizz_acter WHERE id = ?", (rec_id,))

   
    for item in tree3.get_children():
        tree3.delete(item)

    # Загрузка обновленных данных из базы данных
    add_data_on_interface_bizz_acter = conn.execute("SELECT * FROM bizz_acter")
    
    for value_bizz_acter in add_data_on_interface_bizz_acter:
        tree3.insert("", "end", values=value_bizz_acter)
    conn.commit()
    window.destroy()

def del_Z():
    win1 = tkinter.Tk()
    win1.title("Удалить:Занятость актеров в спектакле") 
    win1.geometry("350x350")
    label1= tkinter.Label(win1,text="ID")
    
    ent1 = tkinter.Entry(win1,width=20)

    label1.grid(row=0,column=0)
    ent1.grid(row=0,column=1)

    btn_del = ttk.Button(win1,text="Удалить",command=lambda: cliked_del_Z(win1,ent1))

    btn_del.grid(row=0,column=4) 
#####################################################################################

select_tabel = "Актеры"
def tab_change(event):
    selected_tab = NB.tab(NB.select(), "text")
    global select_tabel
    select_tabel = selected_tab


def def_scr(ent_scr):

    conn = sqlite3.connect("DATABASS.db")
    curs = conn.cursor()
    value_ent = ent_scr.get()
    tab_c = tab_change
    print(select_tabel, value_ent)
    if(select_tabel == "Актеры"):
        
        if("" == value_ent):
            for item in tree1.get_children():
                tree1.delete(item)

            add_data_on_interface_acter=curs.execute("""--sql
            SELECT * FROM acter
                    """)
            
            for value_acter in add_data_on_interface_acter:
                tree1.insert("","end",values=value_acter)




        for item in tree1.get_children():
            tree1.delete(item)

        curs.execute("PRAGMA table_info(acter);")
        columns = [column[1] for column in curs.fetchall()]

# Создаем условие для поиска по всем столбцам
        search_conditions = " OR ".join([f"{col} LIKE ?" for col in columns])
        query = f"SELECT * FROM acter WHERE {search_conditions}"

# Создаем список параметров для запроса
        params = ['%' + value_ent + '%' for _ in columns]

# Выполняем запрос
        add_data_on_interface_acter = curs.execute(query, params)
        
    

        for value_acter in add_data_on_interface_acter:
            tree1.insert("","end",values=value_acter)

        conn.commit()
        

    

    elif (select_tabel == "Спектакли"):
        if("" == value_ent):
            for item in tree2.get_children():
                tree2.delete(item)

            add_data_on_interface_acter=curs.execute("""--sql
            SELECT * FROM spekakl
                    """)
            
            for value_acter in add_data_on_interface_acter:
                tree2.insert("","end",values=value_acter)




        for item in tree2.get_children():
            tree2.delete(item)

        curs.execute("PRAGMA table_info(spekakl);")
        columns = [column[1] for column in curs.fetchall()]

# Создаем условие для поиска по всем столбцам
        search_conditions = " OR ".join([f"{col} LIKE ?" for col in columns])
        query = f"SELECT * FROM spekakl WHERE {search_conditions}"

# Создаем список параметров для запроса
        params = ['%' + value_ent + '%' for _ in columns]

# Выполняем запрос
        add_data_on_interface_acter = curs.execute(query, params)
        
    

        for value_acter in add_data_on_interface_acter:
            tree2.insert("","end",values=value_acter)

        conn.commit()

    elif (select_tabel == "Занятость актеров в спектакле"):
        if("" == value_ent):
            for item in tree3.get_children():
                tree3.delete(item)

            add_data_on_interface_acter=curs.execute("""--sql
            SELECT * FROM bizz_acter
                    """)
            
            for value_acter in add_data_on_interface_acter:
                tree3.insert("","end",values=value_acter)




        for item in tree3.get_children():
            tree3.delete(item)

        curs.execute("PRAGMA table_info(bizz_acter);")
        columns = [column[1] for column in curs.fetchall()]

# Создаем условие для поиска по всем столбцам
        search_conditions = " OR ".join([f"{col} LIKE ?" for col in columns])
        query = f"SELECT * FROM bizz_acter WHERE {search_conditions}"

# Создаем список параметров для запроса
        params = ['%' + value_ent + '%' for _ in columns]

# Выполняем запрос
        add_data_on_interface_acter = curs.execute(query, params)
        
    

        for value_acter in add_data_on_interface_acter:
            tree3.insert("","end",values=value_acter)

        conn.commit()


