class Model:

	WORK = 'WORK'
	BREAK = 'BREAK'
	LONG_BREAK = 'LONG BREAK'

	def __init__(self):

		self.mode = Model.WORK

		# self.work_time = 25*60
		self.work_time = 1
		
		# self.break_time = 5*60
		self.break_time = 2
		
		# self.long_break_time = 10*60
		self.long_break_time = 3


		self.work_break_reps = 2
		self.work_break_counter = 0
