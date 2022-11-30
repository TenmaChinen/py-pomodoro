from .utils import brightess
from tkinter import Button

d_btn_play_style = dict(fg='white', activeforeground='#FFDFDF', bd=0, font=(
    'Calibri', 60, 'bold'), relief='flat')

d_btn_tab_style = dict(fg='white', activeforeground='#FFDFDF', bd=0, font=(
    'Calibri', 18, 'bold'), relief='flat', padx=5, pady=5)

d_btn_settings_style = dict(fg='white', activeforeground='#FFDFDF', bd=0, font=(
    'Calibri', 20, 'bold'), relief='flat')


class ButtonPlay(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master, cnf=d_btn_play_style, **kw)
        self.config(text='▶', bg=master['bg'], activebackground=master['bg'])
        self['command'] = self.__on_click
        self.place(anchor='center')
        self.state = False
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def __on_click(self):
        self.state = not self.state
        self['text'] = '||' if self.state else '▶'
        if self.callback:
            self.callback(self.state)

    def set_state(self, state):
        self.state = state
        self['text'] = '||' if self.state else '▶'


class ButtonTab(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master, cnf=d_btn_tab_style, **kw)
        self['bg'] = master['bg']
        self['activebackground'] = brightess(master['bg'], 0.95)
        self.grid(sticky='news')


class ButtonSettings(Button):
     def __init__(self, master, **kw):
        Button.__init__(self, master, cnf=d_btn_settings_style, **kw)
        self.config(text='⚙', bg=master['bg'], activebackground=master['bg'])
        self.place(relx=1,rely=0, anchor='ne')


d_btn_save = dict(fg='white', activeforeground='#E4B6B6',
                  bd=0, font=('Calibri', 20, 'bold'), relief='flat')


class ButtonSave(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master, cnf=d_btn_save, **kw)
        self.config(text='Save', bg = master['bg'], activebackground = master['bg'])

d_btn_close = dict(fg='white', bg='#535353', activeforeground='#383838',
                   bd=0, font=('Calibri', 20, 'bold'), relief='raised')

class ButtonClose(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master, cnf=d_btn_close, **kw)
        self['text'] = '✖'
        self['bg'] = master['bg']
        self['activebackground'] = master['bg']