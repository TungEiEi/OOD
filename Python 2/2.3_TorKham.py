class TorKham:
	def __init__(self):
		self.command_set = []
		self.words = []

	def restart(self):
		self.words.clear()
		return print("game restarted")
	
	def play(self):
		run = True
		while run:
			for command in self.command_set:
				if ('R'== command):
					self.restart()
				elif ('X'== command):
					run = False
				elif ('P' == command[0]):
					self.words.append(command[2:])
					for word in self.words:
						if (word[-2:].upper() != command[2:4].upper() and word != command[2:]):							
							return print(f"'{command[2:]}' -> game over")
						else:
							print(f"'{command[2:]}' -> {self.words}")
							break
				else:
					return	print(f"'{command}' is Invalid Input !!!")



torkham = TorKham()


print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
torkham.command_set = S
torkham.play()