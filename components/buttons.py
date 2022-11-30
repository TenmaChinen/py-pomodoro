from tkinter import Button

d_btn_style_a = dict(fg='white', activeforeground='#FFDFDF', bd=0, font=(
    'Calibri', 60, 'bold'), relief='flat')

d_btn_style_b = dict(fg='white', activeforeground='#FFDFDF', bd=0, font=(
    'Calibri', 18, 'bold'), relief='flat', padx=5, pady=5)


class ButtonPlay(Button):
    def __init__ (self,master,**kw):
        Button.__init__(self,master,cnf=d_btn_style_a,**kw)
        self.config( text = '▶', bg= master['bg'], activebackground=master['bg'])
        self['command'] = self.__on_click
        self.place(anchor='center')
        self.state = False
        self.callback = None

    def set_callback(self,callback):
        self.callback = callback

    def __on_click(self):
        self.state = not self.state
        self['text'] = '||' if self.state else '▶'
        if self.callback:
            self.callback(self.state)

    def set_state(self,state):
        self.state = state
        self['text'] = '||' if self.state else '▶'

class ButtonB(Button):
    def __init__ (self,master,**kw):
        Button.__init__(self,master,cnf=d_btn_style_b,**kw)
        self['bg'] = master['bg']
        self['activebackground'] = brightess(master['bg'],0.95)
        self.grid(sticky='news')


from colorsys import rgb_to_hls, hls_to_rgb

def brightess(hex_color,pct):
    hex_color = hex_color.strip('#')
    r,g,b = [ int(hex_color[i:i+2],16) for i in range(0,6,2)]
    h, l, s = rgb_to_hls(r,g,b)
    l = l * pct
    r,g,b = [ int(x) for x in hls_to_rgb(h, l, s)]
    hex_color = '#%02X%02X%02X' % (r,g,b)
    return hex_color
