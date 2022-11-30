from .entries import EntryTime, EntryInt
from tkinter import Frame, Label

d_label_style = dict(fg='#D95550', bd=0, font=('Calibri', 20, 'bold'), relief='flat', padx=5)
d_label_dots_style = dict(fg='#D95550', bd=0, font=('Calibri', 40, 'bold'), relief='flat')

d_entry_style = dict(fg='#D95550', bd=0, font=('Calibri', 35, 'bold'), relief='flat',insertwidth=3, insertborderwidth=0)


class FieldTime(Frame):
    def __init__(self, master, name, **kw):
        Frame.__init__(self, master, **kw)
        self.config(bg=master['bg'], padx=20)
        self.__create_label(name)
        self.fr_entries = self.__create_frame_entries()
        self.et_mins = self.__create_entry_minutes()
        self.__create_label_dots()
        self.et_secs = self.__create_entry_seconds()

    def __create_label(self, name):
        label = Label(master=self, text=name, cnf=d_label_style)
        label.config(bg=self['bg'], width = 12)
        label.pack(side='left', fill='y')

    def __create_frame_entries(self):
        frame_entries = Frame(master=self)
        frame_entries.config(bg=self['bg'])
        frame_entries.pack(side='left')
        return frame_entries

    def __create_entry_minutes(self):
        entry_minutes = EntryTime(master=self.fr_entries)
        entry_minutes.pack(side='left')
        return entry_minutes

    def __create_label_dots(self):
        label = Label(master=self.fr_entries,text=':', cnf=d_label_dots_style)
        label.config(bg=self['bg'])
        label.pack(side='left', padx=5)

    def __create_entry_seconds(self):
        entry_seconds = EntryTime(master=self.fr_entries)
        entry_seconds.pack(side='left')
        return entry_seconds

    # Methods

    def set_callback(self, callback):
        self.callback = callback

    def get_time(self):
        ''' time in seconds '''
        return self.et_mins.get_value() * 60 + self.et_secs.get_value()

    def set_time(self,seconds):
        minutes, seconds = divmod(seconds, 60)
        self.et_mins.set_value(minutes)
        self.et_secs.set_value(seconds)


class FieldValue(Frame):
    
    def __init__(self, master, name, **kw):
        Frame.__init__(self, master, **kw)
        self.config(bg=master['bg'], padx=20)
        self.__create_label(name)
        self.et_value = self.__create_entry_value()

    def __create_label(self, name):
        label = Label(master=self, text=name, cnf=d_label_style)
        label.config(width = 12, bg=self['bg'])
        label.pack(side='left', fill='y')

    def __create_entry_value(self):
        entry_value = EntryInt(master=self, limits=(1,99))
        entry_value.pack(side='left')
        return entry_value

    # Methods

    def get_value(self):
        return self.et_value.get_value()

    def set_value(self,value):
        self.et_value.set_value(value)