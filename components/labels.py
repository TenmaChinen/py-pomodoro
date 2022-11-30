from tkinter import Label

d_lbl_style_a = dict(fg='white', font=('Calibri', 90, 'bold'))
d_lbl_style_b = dict(fg='white', font=('Calibri', 40, 'bold'))

class LabelMinSecs(Label):
    def __init__ (self,master,**kw):
        Label.__init__(self,master,cnf=d_lbl_style_a,**kw)
        self['bg'] = master['bg']
        self.place(anchor='center')

class LabelStatus(Label):
    def __init__ (self,master,**kw):
        Label.__init__(self,master,cnf=d_lbl_style_b,**kw)
        self['bg'] = master['bg']
        self.place(anchor='center')