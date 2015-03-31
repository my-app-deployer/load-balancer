""" 
This class is used for creating the slave for the master
A slave is a Node
A slave has only 1 master
"""
from loadbalancer import Node
class Slave(Node):
	"""docstring for Slave"""
	def __init__(self, arg):
		super(Slave, self).__init__()
		self.arg = arg
	def getActivity():
		pass
	def getState():
		pass
		