class Crash(object):
	
	def __init__(self, value):
		self.value = value
	
	@staticmethod
	def show(self):
		pass
		
	@property
	def balance(self):
		return '${:.2f}'.format(self.value)
	
	@balance.setter
	def balance(self, new_value):
		self.value = float(new_value)


crash1 = Crash(10.2)
print(crash1.balance)

crash1.balance = 1000
print(crash1.balance)

print(crash1.value)
