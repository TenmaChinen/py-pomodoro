from time import sleep

class Timer:

    def __init__(self,string_var):
        self.string_var = string_var
        self.root = string_var._root
        self.running = False
        self.callback = None
        self.top_count = 0
        self.remaining_time = 0
        self.after_id = None

    def set_callback(self,callback):
        self.callback = callback

    def set_timer(self,time):
        self.top_count = time
        self.remaining_time = time
        self.running = False
        self.__after_cancel()
        self.update_variable()

    def start(self):
        if self.remaining_time != 0:
            self.running = True
            if not self.after_id:
                self.after_id = self.root.after(1000, self.__update_timer)

    def stop(self):
        self.running = False
        self.__after_cancel()

    def restart(self):
        self.__after_cancel()
        self.running = False
        self.remaining_time = self.top_count
        self.update_variable()

    def __after_cancel(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None

    def __update_timer(self):

        if self.running:

            if self.remaining_time > 0:
                self.remaining_time -= 1
                self.update_variable()
                self.after_id = self.root.after(1000, self.__update_timer)

            elif self.remaining_time == 0:
                self.running = False
                if self.callback:
                    self.callback()

    def update_variable(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.string_var.set(f'{minutes:02d}:{seconds:02d}')