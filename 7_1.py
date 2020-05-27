class Singleton(type): 
	__instance= None 
	
	def __new__(cls, *args, **kwarg): 
		if Singleton.__instance is None: 
			Singleton.__instance = object.__new__(cls)
		return Singleton.__instance
	
	def __init__ (self, a, b): 
		self.a = a
		self.b = b 

first = Singleton(1,2) 

#second = Singleton (3,4) 

#print (second.a)
