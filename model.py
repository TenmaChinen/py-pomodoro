import json
import os

class Model:

    WORK = 'WORK'
    BREAK = 'BREAK'
    LONG_BREAK = 'LONG BREAK'
    PATH_SETTINGS = 'storage/settings.json'

    def __init__(self):

        self.mode = Model.WORK
        self.work_break_counter = 0
        self.load_settings()

    def load_settings(self):
        if os.path.exists(Model.PATH_SETTINGS):
            self.d_settings = load_json(path=Model.PATH_SETTINGS)
        else:
            self.d_settings = {
                'work_time' : 25*60,
                'break_time' : 5*60,
                'long_break_time' : 10*60,
                'work_break_reps' : 2
            }
            self.save_settings()

    def save_settings(self):
        save_json(path=Model.PATH_SETTINGS, data=self.d_settings)
            


def load_json(path):
    file = open(path,'r')
    data = json.load(file)
    file.close()
    return data

def save_json(path,data):
    file = open(path,'w')
    json.dump(data, file)
    file.close()