from tkinter import Frame, Label, Entry
from .utils import brightess

d_entry_style = dict(fg='#D95550', bd=0, font=('Calibri', 35, 'bold'), relief='flat',insertwidth=3, insertborderwidth=0)

class ActionType:
    INSERT = '1'
    DELETE = '0'

class EntryTime(Entry):

    def __init__(self, master, **kw):
        Entry.__init__(self, master, cnf=d_entry_style, **kw)
        self.config(bg=master['bg'], width=2, insertbackground=self['fg'], selectbackground=brightess(self['fg'],1.3))
        self.__set_validation(root=master._root())
        self.__create_underline()
        self.__set_binding()
        self.set_value(0)

    def __set_validation(self, root):
        self.vcmd = (root.register(self.__on_validate), '%P', '%i', '%d', '%S', '%s')
        self.config(validate='key', validatecommand=self.vcmd)

    def __create_underline(self):
        fr_underline = Frame(master=self, height=4, bg=self['fg'])
        fr_underline.place(in_=self, relx=0.5, rely=1, relwidth=1, anchor='s')

    def __set_binding(self):
        self.bind('<FocusOut>', self.__on_focus_out)

    def __format(self,value):
        return f'{value:02d}'

    # Methods
    
    def set_value(self,value):
        self.delete(0,'end')
        text = self.__format(value)
        self.insert(0,text)

    def get_value(self):
        return int(self.get())
    
    # Callbacks

    def __on_focus_out(self,event):
        value = self.get_value()
        self.set_value(value)

    def __on_validate(self, text, idx, action_type, in_char, old):
        idx = int(idx)
        
        if action_type == ActionType.DELETE and idx == 0:
            return True
        
        try:
            return len(text) < 3 and int(text) < 60
        except BaseException as e:
            return False


class EntryInt(Entry):

    def __init__(self, master, limits=(1,99), **kw):
        Entry.__init__(self, master, cnf=d_entry_style, **kw)
        self.config(bg=master['bg'], width=2, justify='center', insertbackground=self['fg'], selectbackground=brightess(self['fg'],1.3))
        self.__create_underline()
        self.__set_validation(root=master._root())
        self.__set_binding()
        self.set_value(0)
        self.lim_min, self.lim_max = limits

    def __set_validation(self, root):
        self.vcmd = (root.register(self.__on_validate), '%P', '%i', '%d')
        self.config(validate='key', validatecommand=self.vcmd)

    def __create_underline(self):
        fr_underline = Frame(master=self, height=4, bg=self['fg'])
        fr_underline.place(in_=self, relx=0.5, rely=1, relwidth=1, anchor='s')


    def __set_binding(self):
        self.bind('<FocusOut>', self.__on_focus_out)

    # Methods
    
    def set_value(self,value):
        self.delete(0,'end')
        self.insert(0,value)

    def get_value(self):
        if self.get() == '':
            self.set_value(self.lim_min)
        return int(self.get())
    
    # Callbacks

    def __on_focus_out(self,event):
        if self.get() == '':
            self.set_value(self.lim_min)

    def __on_validate(self, text, idx, action_type):

        if action_type == ActionType.DELETE and idx == '0':
            return True
        
        try:
            value = int(text)
            return value >= self.lim_min and value <= self.lim_max
        except:
            return False