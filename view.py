from components.buttons import ButtonPlay, ButtonTab, ButtonSettings
from components.labels import LabelMinSecs, LabelStatus
from components.dialogs import DialogSettings
from tkinter import Tk, StringVar, Frame
from components.timer import Timer

BG_1 = '#D95550'
BG_2 = '#BA3D3D'

class View:

    WORK = 'WORK'
    BREAK = 'BREAK'
    LONG_BREAK = 'LONG BREAK'
    STOPPED = 'STOPPED'

    def __init__(self):
        self.root = self.__create_root()
        self.__create_variables()
        self.timer = self.__create_timer()
        self.lbl_min_sec = self.__create_label_minutes_seconds()
        self.btn_play = self.__create_button_play()
        self.btn_settings = self.__create_button_settings()
        self.lbl_status = self.__create_label_status()
        self.__create_frame_buttons()
        self.dialog_settings = self.__create_dialog_settings()

    def __create_root(self):
        # GUI window configuration
        root = Tk()
        root.geometry('400x650+50+50')
        root.resizable(False, False)
        root.title('Pomodoro')
        root.config(bg=BG_1)
        root.iconbitmap('assets/images/pomodoro.ico')
        # DEBUG PURPOSES
        root.bind_all('<Control-q>', lambda e : root.destroy())
        root.protocol('WM_DELETE_WINDOW', self.__on_closing)
        return root

    def __create_variables(self):

        self.work_time = 3
        self.break_time = 3

        # label
        self.min_sec = StringVar(self.root)
        self.min_sec.set('00:00')
        
        self.status = StringVar(self.root)
        self.status.set(View.WORK)
    
    def __create_timer(self):
        timer = Timer(string_var=self.min_sec)
        timer.set_callback(callback=self.__on_timeout)
        return timer

    def __create_label_minutes_seconds(self):
        lbl_min_sec = LabelMinSecs(self.root, textvariable=self.min_sec)
        lbl_min_sec.place(relx=0.5, rely=0.2)
        return lbl_min_sec

    def __create_button_settings(self):
        btn_settings = ButtonSettings(master=self.root)
        btn_settings['command'] = self.__on_click_settings

    def __create_button_play(self):
        btn_play = ButtonPlay(master=self.root)
        btn_play.set_callback(callback=self.__on_click_play)
        btn_play.place(relx=0.5, rely=0.5)
        return btn_play

    def __create_label_status(self):
        lbl_status = LabelStatus(master=self.root, textvariable=self.status)
        lbl_status.place(relx=0.5, rely=0.7)
        return lbl_status

    def __create_frame_buttons(self):
        fr_buttons = Frame(self.root, bg=BG_2, height=250)
        fr_buttons.place(relwidth=1.0, relx=0.5, rely=1.0, anchor='s')
        
        for idx in range(3):
            fr_buttons.grid_columnconfigure(idx, weight=1, uniform='column')

        self.btn_work = ButtonTab(master=fr_buttons, text='WORK')
        self.btn_work['command'] = lambda : self.__on_click_frame_buttons(View.WORK)
        self.btn_work.grid(row=0, column=0)
        
        self.btn_break = ButtonTab(master=fr_buttons, text='BREAK')
        self.btn_break['command'] = lambda : self.__on_click_frame_buttons(View.BREAK)
        self.btn_break.grid(row=0, column=1)
        
        self.btn_long_break = ButtonTab(master=fr_buttons, text='L-BREAK')
        self.btn_long_break['command'] = lambda : self.__on_click_frame_buttons(View.LONG_BREAK)
        self.btn_long_break.grid(row=0, column=2)

    def __create_dialog_settings(self):
        dialog_settings = DialogSettings(master=self.root)
        dialog_settings.set_callback(callback=self.__on_dialog_click_save)
        return dialog_settings


    # Methods

    def set_controller(self,controller):
        self.controller = controller

    def set_status(self,status):
        self.status.set(value=status)
        self.timer.update_variable()

    def _set_window_on_top(self):
        self.root.attributes('-topmost', True)
        self.root.attributes('-topmost', False)


    # Callbacks
    def __on_closing(self):
        self.running = False
        self.root.destroy()

    def __on_click_frame_buttons(self,btn_type):
        self.status.set(btn_type)
        self.controller.on_click_frame_button(btn_type)

    def __on_click_settings(self):
        self.controller.on_click_settings()

    def __on_click_play(self,state):
        self.controller.on_click_play(state)

    def __on_timeout(self):
        self.controller.on_timeout()

    def __on_dialog_click_save(self,d_data):
        self.controller.on_dialog_click_save(d_data)
