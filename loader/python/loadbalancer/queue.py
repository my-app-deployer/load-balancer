""" 
This class is used for creating/reading jobs from a mongoDB queue
"""
import PyMongo
class Queue(object):
	"""docstring for Queue"""
	def __init__(self, arg):
		super(Queue, self).__init__()
		self.arg = arg
	def read(self):
		pass
	def subscribe(self):
		pass
	def publish(self):
		pass
		