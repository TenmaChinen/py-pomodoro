from .buttons import ButtonClose, ButtonSave
from .fields import FieldTime, FieldValue
from tkinter import Frame

d_frame_style = dict(bd=1)
d_fr_body_style = dict(bg='white')
d_fr_footer_style = dict(bg='#D95550')

class DialogSettings(Frame):
    def __init__ (self,master,**kw):
        Frame.__init__(self,master,cnf=d_frame_style,**kw)
        self.__create_frame_header()
        self.fr_body = self.__create_frame_body()
        self.fr_footer = self.__create_frame_footer()
        self.field_work_time = self.__create_field_work_time()
        self.field_break_time = self.__create_field_break_time()
        self.field_long_break_time = self.__create_field_long_break_time()
        self.field_work_break_reps = self.__create_field_work_break_reps()
        self.__create_button_save()
        self.callback = None

    def __create_frame_header(self):
        fr_header = Frame(master=self, bg='#BC443F')
        fr_header.pack(side='top', fill='x')
        
        btn_close = ButtonClose(master=fr_header)
        btn_close['command'] = self.__on_click_close
        btn_close.pack(side='right', fill='y')

    def __create_frame_body(self):
        fr_body = Frame(master=self, cnf=d_fr_body_style)
        fr_body.pack(side='top', fill='both', expand=True)
        return fr_body

    def __create_frame_footer(self):
        fr_footer = Frame(master=self, cnf=d_fr_footer_style)
        fr_footer.pack(side='top', fill='x')
        return fr_footer

    def __create_field_work_time(self):
        field_work_time = FieldTime(master=self.fr_body, name='Work Time')
        field_work_time.pack(side='top', fill='x', expand=True)
        return field_work_time

    def __create_field_break_time(self):
        field_break_time = FieldTime(master=self.fr_body, name='Break Time')
        field_break_time.pack(side='top', fill='x', expand=True)
        return field_break_time

    def __create_field_long_break_time(self):
        field_long_break_time = FieldTime(master=self.fr_body, name='Long\nBreak Time')
        field_long_break_time.pack(side='top', fill='x', expand=True)
        return field_long_break_time

    def __create_field_work_break_reps(self):
        field_work_break_reps = FieldValue(master=self.fr_body, name='Reps for\nLong Break')
        field_work_break_reps.pack(side='top', fill='x', expand=True, pady=100)
        field_work_break_reps.set_value(value=2)
        return field_work_break_reps

    def __create_button_save(self):
        btn_save = ButtonSave(master=self.fr_footer)
        btn_save['command'] = self.__on_click_save
        btn_save.pack(side='right', padx=10)

    def __on_click_close(self):
        self.hide()

    def __on_click_save(self):
        if self.callback:
            d_data = dict(
                work_time = self.field_work_time.get_time(),
                break_time = self.field_break_time.get_time(),
                long_break_time = self.field_long_break_time.get_time(),
                work_break_reps = self.field_work_break_reps.get_value(),
                )
            self.callback(d_data)

    # Methods

    def set_callback(self,callback):
        self.callback = callback

    def set_fields(self, d_data):
        self.field_work_time.set_time(d_data['work_time'])
        self.field_break_time.set_time(d_data['break_time'])
        self.field_long_break_time.set_time(d_data['long_break_time'])
        self.field_work_break_reps.set_value(d_data['work_break_reps'])

    def show(self):
        self.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.95, anchor='center')

    def hide(self):
        self.place_forget()
