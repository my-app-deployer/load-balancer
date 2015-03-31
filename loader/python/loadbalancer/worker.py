""" 
This class is used for creating/reading jobs from a redis queue
A master is a Node
"""
class Worker(object):
	"""docstring for Worker"""
	def __init__(self, arg):
		super(Worker, self).__init__()
		self.arg = arg

		