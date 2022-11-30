from winsound import PlaySound, SND_ASYNC


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.set_mode(mode=self.model.WORK)

    def on_click_play(self, state):
        if self.view.timer.remaining_time != 0:
            if state:
                self.view.timer.start()
            else:
                self.view.timer.stop()
        else:
            self.view.btn_play.set_state(False)

    def on_click_frame_button(self, btn_type):

        if btn_type == self.view.WORK:
            self.set_mode(mode=self.model.WORK)
        elif btn_type == self.view.BREAK:
            self.set_mode(mode=self.model.BREAK)
        elif btn_type == self.view.LONG_BREAK:
            self.set_mode(mode=self.model.LONG_BREAK)

    def set_mode(self, mode):
        d_settings = self.model.d_settings

        if mode == self.model.WORK:
            self.view.timer.set_timer(time=d_settings['work_time'])
        elif mode == self.model.BREAK:
            self.view.timer.set_timer(time=d_settings['break_time'])
        elif mode == self.model.LONG_BREAK:
            self.view.timer.set_timer(time=d_settings['long_break_time'])

        self.model.mode = mode
        self.view.btn_play.set_state(False)
        self.view.set_status(mode)

    def on_timeout(self):
        self.view.btn_play.set_state(False)
        PlaySound('sounds/birds.wav', SND_ASYNC)

        if self.model.mode == self.model.WORK:

            if self.model.work_break_counter == self.model.work_break_reps:
                self.set_mode(self.model.LONG_BREAK)
            else:
                self.set_mode(self.model.BREAK)

        elif self.model.mode == self.model.BREAK:
            self.model.work_break_counter += 1
            self.set_mode(self.model.WORK)

        elif self.model.mode == self.model.LONG_BREAK:
            self.model.work_break_counter = 0
            self.set_mode(self.model.WORK)

        self.view.timer.start()


    def on_click_settings(self):
        self.view.dialog_settings.set_fields(d_data=self.model.d_settings)
        self.view.dialog_settings.show()

    def on_dialog_click_save(self,d_data):
        self.model.d_settings = d_data
        self.view.dialog_settings.hide()
        self.model.save_settings()
        # print(d_settings)