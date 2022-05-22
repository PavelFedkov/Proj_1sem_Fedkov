import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/1.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить заказ', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="img/2.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="img/3.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="img/4.png")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="img/5.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'client', 'master', 'izdelie', 'material', 'stoim'),
                                 height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('client', width=180, anchor=tk.CENTER)
        self.tree.column('master', width=140, anchor=tk.CENTER)
        self.tree.column('izdelie', width=140, anchor=tk.CENTER)
        self.tree.column('material', width=140, anchor=tk.CENTER)
        self.tree.column('stoim', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('client', text='ФИО клиента')
        self.tree.heading('master', text='ФИО мастера')
        self.tree.heading('izdelie', text='Вид изделия')
        self.tree.heading('material', text='Материал')
        self.tree.heading('stoim', text='Стоимость работы')

        self.tree.pack()

    def records(self, user_id, client, master, izdelie, material, stoim):
        self.db.insert_data(user_id, client, master, izdelie, material, stoim)
        self.view_records()

    def update_record(self, user_id, client, master, izdelie, material, stoim):
        self.db.cur.execute(
            """UPDATE users SET user_id=?, client=?, master=?, izdelie=?, material=?, stoim=? WHERE user_id=?""",
            (user_id, client, master, izdelie, material, stoim, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE user_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    # def search_records(self, user_id):
    #     user_id = ("%" + user_id + "%",)
    #     self.db.cur.execute("""SELECT * FROM users WHERE name LIKE ?""", user_id)
    #     [self.tree.delete(i) for i in self.tree.get_children()]
    #     [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def search_records(self, master):
        master = (master,)
        self.db.cur.execute("""SELECT * FROM users WHERE master=?""", master)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить клиента')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер')
        label_description.place(x=50, y=20)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=150, y=20)

        label_name = tk.Label(self, text='Имя клиента')
        label_name.place(x=50, y=45)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=150, y=45)

        label_name_mastera = tk.Label(self, text='Имя мастера')
        label_name_mastera.place(x=50, y=70)
        self.entry_name_mastera = ttk.Entry(self)
        self.entry_name_mastera.place(x=150, y=70)

        label_izdelie = tk.Label(self, text='Изделие')
        label_izdelie.place(x=50, y=95)
        self.entry_izdelie = ttk.Entry(self)
        self.entry_izdelie.place(x=150, y=95)

        label_mater = tk.Label(self, text='Материал')
        label_mater.place(x=50, y=120)
        self.entry_mater = ttk.Entry(self)
        self.entry_mater.place(x=150, y=120)

        label_stoim = tk.Label(self, text='Стоимость')
        label_stoim.place(x=50, y=145)
        self.entry_stoim = ttk.Entry(self)
        self.entry_stoim.place(x=150, y=145)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_name_mastera.get(),
                                                                       self.entry_izdelie.get(),
                                                                       self.entry_mater.get(),
                                                                       self.entry_stoim.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_name_mastera.get(),
                                                                          self.entry_izdelie.get(),
                                                                          self.entry_mater.get(),
                                                                          self.entry_stoim.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('saper.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client TEXT NOT NULL,
                master INTEGER NOT NULL DEFAULT 1,
                izdelie INTEGER,
                material INTEGER,
                stoim INTEGER
                )""")

    def insert_data(self, user_id, client, master, izdelie, material, stoim):
        self.cur.execute(
            """INSERT INTO users(user_id, client, master, izdelie, material, stoim) VALUES (?, ?, ?, ?, ?, ?)""",
            (user_id, client, master, izdelie, material, stoim))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Ювелирная мастерская")
    root.geometry("790x450+300+200")
    root.resizable(False, False)
    root.mainloop()
