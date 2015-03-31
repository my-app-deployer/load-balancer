""" 
This class is used for creating the master that will rule multiple slaves
A master is a Node
A master can create slaves and monitor them
"""
from loadbalancer import Node
class Master(Node):
	"""docstring for Master"""
	def __init__(self, port):
		self.port=port #The port on which the master must listen
	def getSlave():
		pass
	def isSlaveOccupied():
		pass
	def createSlave():
		pass
	
		