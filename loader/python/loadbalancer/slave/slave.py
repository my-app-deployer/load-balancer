""" 
This class is used for creating the slave for the master
A slave is a Node
A slave has only 1 master
A slave is either an application or a database
"""
from loadbalancer import Node
class Slave(Node):
	"""docstring for Slave"""
	def __init__(self, arg):
		super(Slave, self).__init__()
		self.arg = arg
	def getWorkload(self):
		pass
	def getState(self):
		pass
	def getType(self): #get the type of slave ApplicationDeploy|DatabaseDeploy
		pass
